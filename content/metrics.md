title: It's not about the number of vulnerabilities. It's about the risk.
date: 2021-05-20
modified: 2021-05-20
category: Security
slug: its-not-about-number-of-vulnerabilities-its-about-the-risk
author: Florencio Cano
tags: metrics,risk,vulnerabilities

These are my thoughts about vulnerability management metrics after reading [Business-friendly vulnerability management metrics](https://medium.com/uber-security-privacy/business-friendly-vulnerability-management-metrics-cfd702fd7705).

The metrics described in the article above mainly measure the time that our assets have been vulnerable, taking into account the intensity (the number of vulnerabilities). The information of vulnerabilities is taken from vulnerability scanners.

My opinion about how to measure the risk we face due to vulnerabilities is different.

If I'm the person accountable for the risk of being affected by the exploitation of a vulnerability, what really matters to me is the real probability of a vulnerability being exploited, and the damage that can be done with it, and not the quantity of vulnerabilities or the time they are open. What I want to measure and control very well are the really dangerous vulnerabilities. So, I think we should focus on "quality" of the vulnerabilities, and not the number of them.

When we measure people about the number of vulnerabilities, they tend to fix more vulnerabilities. But that is not what we want to reduce the risk in an effective way. We want that they fix the vulnerabilities which have more probability of being exploited and that can cause more damage to my organization. I prefer that they fix much less vulnerabilities, but more important.

In order to determine how important is a vulnerability, we have to think about the probability of exploitation and the damage (impact) it would cause if it is successfully exploited. In order to do this, we have to take into account if the vulnerability is exploitable from the outside of the company or only from the inside. Also, if in order to exploit the vulnerability the attacker can be unathenticated or if some kind of account or permissions are needed. Also it is important to know if the vulnerability is easy to exploit (if it is trivial to exploit, if there exist exploits in the wild) or if it is difficult (for example vulnerabilities that can be exploited only in theory, only in a lab, only by advanced researchers). We have to think also if there are mitigating security controls that reduce the probability of being exploited or the damage in case they are exploited.

For me, the most critical vulnerability would be a vulnerability that can be exploited from the outside, in a trivial way, and that would give direct access to a critical database (the importance of the asset is another factor that we have to take into account). I prefer to have 1000 internal vulnerabilities difficult to exploit the whole year than one of vulnerability that can be exploited by unathenticated users, from the outside, and that would give access to a credit card database during 1 hour.

These are some metrics that are more interesting for me:

* Time between an Important or Critical vulnerability is public and we know about it.
* Time between an Important or Critical vulnerability is public and we fix or mitigate it (mitigate = reduce to Moderate or Low by applying security controls).
* Time between we have an Important or Critical vulnerability (when not related to third parties, but only affects us, like an insecure configuration) and we know about it.
* Time between we have an Important or Critical vulnerability and we fix or mitigate it.
* Number of Important or Critical vulnerabilities in custom code/config that reach production.
* Number of times we classify a vulnerability as Moderate or Low, but then it is used by a Red Team or malicious actor to attack us or another organization (wrong analysis).

It is true that by doing this analysis we can be wrong and a vulnerability that seems difficult to exploit is exploited and we get hacked. But, it is also true that we have to prioritize our work (time is limited), and we cannot aim to fix all vulnerabilities without prioritizing them.
