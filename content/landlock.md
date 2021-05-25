title: New important security feature in the Linux kernel: Landlock
date: 2021-05-24
modified: 2021-05-24
category: Security
slug: new-important-security-feature-in-linux-kernel-landlock
tags: linux, kernel, landlock
author: Florencio Cano

Landlock is yet another sandoxing mechanism for Linux, but with important differences. Its goal is to make possible to restrict access rights to different Linux elements (e.g. filesystem access), in a secure way, without admin privileges and in a programmatic way (from within the applications code). Because LandLock is a stackable LSM (Linux Security Module), it makes possible to create safe security sandboxes as new security layers, in addition to the existing system-wide access-controls. This kind of sandbox is expected to help mitigate the security impact of bugs or unexpected/malicious behaviors in user space applications. It is important to remark that Landlock empowers any process, included unprivileged ones, to restrict themselves, reducing the potential impact in case of malicious behavior.


## Linux Security Modules (LSMs)

Linux Security Module (LSM) is a framework[6] that provides various security checks to be hooked by the kernel. The name may be confusing as they are not loadable kernel modules. They are selectable at build-time via CONFIG_DEFAULT_SECURITY and can be overridden at boot-time via the "security=..." kernel command line argument.

The primary users of the LSM interface are Mandatory Access Control (MAC) extensions which provide a comprehensive security policy. Examples include SELinux, Smack, Tomoyo, AppArmor, and now, Landlock. Most LSMs choose to extend the capabilities system, building their checks on top of the defined capability hooks, but that is not the case of Landlock[2].

The design of LSM is described in [7].


## Characteristics of Landlock

A key feature of Landlock is that it allows unprivileged users to restrict processes that they run so it can be embeded within the applications themselves. It is not an administrator's mechanism like SELinux, but a user feature. In SELinux or Smack[8], setting policies is a privileged operation.

On the other hand, Seccomp can be used to create sanboxes too, but it is limited. For example, it does not allow to filter system calls based on the paths of files they try to access, what Landlock do allow. By restricting what a running process can do, a Landlock-based sandbox can reduce the attack surface of the kernel and make the exploitation of vulnerabilities harder in general. In fact, Landlock is inspired by seccomp-bpf, but instead of filtering syscalls and their raw arguments, a Landlock rule can restrict the use of kernel objects like file hierarchies. The first versions of Landlock were based on eBPF,  but it isn't anymore [1].

Landlock also takes inspiration from other OS sandbox mechanisms: XNU Sandbox, FreeBSD Capsicum or OpenBSD Pledge/Unveil.

If a sandboxed program try to access anything outside of the given list (defined by a ruleset or many stacked rulesets), the forbidden call returns EPERM error, but the program is not killed [4].

The question is, if a program is able to restrict its access, what prevents the same program to get again the permissions? LSM hooks are purely restrictive. They can reduce access, but cannot increase it[4]. So, unless there's a bug on the implementation, an attacker cannot escape from it.

In its current form it is not possible to restrict some file-related actions accessible through these syscall families: chdir(2), truncate(2), stat(2), flock(2) chmod(2), chown(2) setxattr(2), ioctl(2), fcntl(2). This was intentional to reduce the code to be included in the kernel and to ease its review. Other subsystems are not covered either (e.g. network) [3].

Table from [5].
|            |   Fine-grained control    | Embedded policy   | Unprivileged use  |
|------------|:-------------------------:|:-----------------:|:-----------------:|
|SELinux     | X                         |                   |                   |
|seccomp-bpf |                           | X                 | X                 |
|namespaces  |                           | X                 | ~                 |
|Landlock    | X                         | X                 | X                 |


## How can Landlock be used

The main threat model may be seen as protecting from vulnerable (i.e. malicious) code[3]. But because Landlock policies can be defined by application developers, they also define their own threat model.

For example, if a browser implements Landlock and restricts itself to the files it needs for running, a vulnerability that is exploitable and which allows code execution will have access only to the file hierarchies that are accessible by the Landlock ruleset defined for the browser, but not to all files and binaries accessible by the user that executes the browser process.

With Landlock, one thing is what other MACs allow the process to access and a different thing is what the Landlock allows the process to access. Remember that LSM are stackable and restrictive so if standard permissions allow the process, capabilities allow the process, SELinux allows the process (or is disabled), but Landlock does not allow the process, the result will be that the process is not allowed to do that.

The important thing for me is that with SELinux, the administrator needed to apply the rules for the application to work properly. With Landlock, the rules can be embeded in the application. Each application, in an ideal world, will come with its Landlock rulesets.


## Proof of Concept

Example of a sandbox https://lore.kernel.org/lkml/20200511192156.1618284-10-mic@digikod.net/ ##FIXME{Fix. This seems to be able to launch a process that independently of the privileges of the user, is restricted at kernel level to access files and dirs outside those authorized}

Here can be found an example of how to apply a landlock rule: [https://landlock.io/linux-doc/landlock-v34/userspace-api/landlock.html](https://landlock.io/linux-doc/landlock-v34/userspace-api/landlock.html).


## When will be Landlock available

Landlock will be available in Linux 5.13 ##FIXME{Also for RHEL? RHEL9?}. ##FIXME{How can I test it now?}


# Resources

[1][https://landlock.io/](https://landlock.io/)
[2][https://twitter.com/kees_cook/status/1388758944433147905](https://twitter.com/kees_cook/status/1388758944433147905)
[3][https://lore.kernel.org/lkml/f646e1c7-33cf-333f-070c-0a40ad0468cd@digikod.net/](https://lore.kernel.org/lkml/f646e1c7-33cf-333f-070c-0a40ad0468cd@digikod.net/)
[4] https://lwn.net/Articles/703876/
[5] https://landlock.io/talks/2018-07-04_landlock-pts.pdf
[6] https://www.kernel.org/doc/html/v4.15/admin-guide/LSM/index.html
[7] https://www.usenix.org/legacy/event/sec02/full_papers/wright/wright_html/index.html ##FIXME{Pending}
[8] https://www.kernel.org/doc/html/v4.14/admin-guide/LSM/Smack.html
