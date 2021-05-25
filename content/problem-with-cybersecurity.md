title: Looking for the root cause of current cybersecurity problems
date: 2021-05-21
modified: 2021-05-21
category: Security
slug: looking-for-root-cause-current-cybersecurity-problems
author: Florencio Cano
tags:toc,root-cause-analysis

I love Goldratt books ([The Goal](https://www.goodreads.com/book/show/113934.The_Goal), [It's Not Luck](https://www.goodreads.com/book/show/157385.It_s_Not_Luck?from_search=true&from_srp=true&qid=dQEjWkU3CN&rank=1), [The Choice](https://www.goodreads.com/book/show/4845427-the-choice?ac=1&from_search=true&qid=FWBh4M06P9&rank=3), [Critical Chain](https://www.goodreads.com/book/show/848514.Critical_Chain)), its Theory of Constraints (TOC) and his thinking tools. One of the thinking tools is called the Current Reality Tree (CRT). It is used when you are trying to find the root problem of a complex problem. In this case, just out of curiosity, I have tried to write a CRT for the problem of cybersecurity: Why are big and important companies are having severe cybersecurity breaches? What can we do to improve this situation?

I'm not going to explain how to design a CRT. I'm not even an expert and this probably has conceptual errors. I will fix it with time, while I improve how to write CRTs. In this post, I'm going to show mine and explain it. What you need to know is that an arrow from A to B means that A causes B. Another way of saying it, is to say that A is a necessary condition for B to happen. If we eliminate A, B will not happen.  If there is an ellipse on top of multiple arrows, it means that all the causes (A, A', A'') must be met for B to happen. Eliminating one, eliminates B. If there are multiple incoming arrows without an ellipse, that is an "or", so you would need to eliminate all the As to B not to happen.

On the top of the tree we have the undesirable effects (UDEs). UDEs are what we see that is not working well and what we want to solve.

The CRT does not state any solutions, only facts (causes of the UDEs, causes of the causes of the UDEs, etc.). The last causes, those on the bottom, without incoming arrows (except reinforcing loops), are the root causes. That means that if we solve the root causes, we will solve the problems derived from them.

Goldratt's principle of Inherent Simplicity states that any complex problem, at the end, only have a few (probably one or two) root causes. If true, that is fantastic, because it means that the tree is not infinite or that it is not more complex when you grow it downwards, but the contrary, you make it more easy because at the bottom there will be less causes, not more.

This is the CRT that I wrote for the cybersecurity problem:

<img alt="Cybersecurity CRT" src="/images/cybersecurity_crt.jpg" width="780px">

# Explanation of the CRT

## Companies continue having severe cybersecurity incidents

Our main and starting UDE is on the top: **Companies continue having severe cybersecurity incidents**. That is a fact. But, what are the reasons? For me, the first direct reason, we may like it or not, is that **Companies don't have enough cybersecurity controls**. If they had enough cybersecurity controls, independently of everything else, severe cybersecurity incidents won't happen.

**Companies don't have enough cybersecurity controls** due to one or more of these reasons:

- Companies don't know how to secure their systems.
- Companies don't want to secure their systems.
- Companies don't know they need to secure their systems.

## Companies don't know how to secure their systems

One of the causes of **Companies continue having severe cybersecurity incidents** is that **Companies don't know how to secure their systems**. They don't know what security controls would reduce the probability or the impact of a security threat to materialize in their company and cause severe damage. In the case of ransomware, that is the most pervasive and damaging security threat currently, this means that companies don't know which security controls they have to implement to avoid the ransomware to infect their systems, propagate, and ransom their data.

I see two reasons why companies don't have this information:

- Companies don't have people who know how to secure their systems.
- Companies don't have people whose mission is to secure their systems.

Let's go down following the path of causes-effects that explain why "Companies don't have people who know how to secure their systems".

## Companies don't have people who know how to secure their systems

Why people that are dedicated to security don't know which security measures can be implemented to reduce the risk of a security breach to acceptable levels? I know that in many cases these professional do know what to do, but the company don't let them do it. That is another branch under "Companies don't want to secure their systems", so we are not talking about this case here. Here I'm talking about not really knowing how to protect the organization against this.

I have thought about two reasons:

- Lack of cybersecurity people trained in technical security controls.
- People who has the mission of securing the organization systems are not cybersecurity professionals.

The second case happens when management has heard something about security, maybe in the news or maybe because they need to comply with some regulation related to security, and they assign one IT person, that is not a security professional, to be in charge of security. This happens usually because "Management and IT is not aware of the importance of having cybersecurity professionals in the team" and that happens, in general, because there is a "Lack of management cybersecurity awareness".

Let's continue with the other branch.

## Lack of cybersecurity people trained in technical security controls

Why there is a "Lack of cybersecurity people trained in technical security controls"? I think the reason is that these cybersecurity people are not trainned. But, why? I see two possible reasons:

- Cybersecurity people think that they don't need to get training.
- Lack of good and cheap training material.

"Cybersecurity people they don't need to get training" is being reinforced by the fact that "Lack of cybersecurity people trained in technical security controls". The less training, the less you think you need training. Dunning-Kruger effect in action. The CRT theory says that reinforcing loops like this are really powerful and we should focus on them when we want to find solutions.

About the second, I'm not completely sure about that. Maybe the material is there but people don't know it or they don't do the effort of reading and studying it. In any case, the reason for these two cases, in my opinion, is the same. We have a "Cybersecurity community that rewards more the image than the knowledge". Some security rock stars that have been appearing in mass media have sent the message that security is cool and easy, without giving credit or raising awareness of the effort required to be a good security professional.

Here we have finished. Let's return to the top of the tree, to the second big reason why Companies don't have enough security controls.

## Companies don't want to secure their systems

Are there companies that don't want to secure their systems? Yes. And they have reasons. Ignoring or undervalue their reasons are not going to help. In this part of the tree I'm going to explore that.

I see this possible reasons:

- Companies don't want to spend budget in cybersecurity.
- Companies do think it is ok to spend budget, but all the cybersecurity controls they know affect negatively on the business (e.g. to its agility).

Let's start with the second, which cause is clear for me and we have already talked about it: Companies don't have people that know how secure their systems. To think about security measures that are aligned with the business is difficult and it takes effort. They are not usually straighfoward. You have to take what books say and transform and adapt those recommendations. Cybersecurity professionals without the needed training tends to try to enforce security measures as they appear in the books, without taking the business into account.

Well trained security professionals look for for the best solutions for the business which usually are non trivial solutions that do not affect negatively the business or whose negative impact is clearly worth it and makes sense.

## Companies don't want to spend money on cybersecurity

Let's explore now why companies don't want to spend money on cybersecurity. Companies spend money in things they think they need. So, the reason is clear: the company (management) thinks that cybersecurity is not necessary so they choose to not spend money or time in cybersecurity. In my opinion, management thinks so because they are not aware of the security risks. They are usually very busy, and they need people around them that explains them what they need to know in a very easy straighforward way. Here we have a reinforcing cycle again...because companies don't have people whose mission is security, management don't have people around them that talk about security and explain it and make the risks visible.

There is one more reason that explains why management are not aware of cybersecurity risks: in the cases that the company have cybersecurity people, sometimes, these cybersecurity people don't know how to talk about risks to management. Cybersecurity people is usually technical people. And we, technical people, do have in general a problem for explaining things in an easy understandable way. The reason for this is again lack of good cybersecurity training or lack of training aimed to talk about risks and how cyber risks affect companies.

## Companies don't know how they need to protect their assets

This is the third reason why Companies don't have enough cybersecurity controls. The main reason for this, almost a synonim, is that management is not aware of the risks and we have already talked about the reasons.

# Root causes and solutions

At the end, based on the logic explained, we have that the root causes of "Companies continue having severe cybersecurity incidents" are:

- Security community that rewards image over knowledge.
- Lack of management cybersecurity awareness.

Let's talk about solutions.

For the second root cause, "Lack of management cybersecurity awareness", I think it is something that will improve with time. If cybersecurity is as important as we think it is, the number of security incidents will raise the awareness in a natural way. In my opinion, current security incidents due to ransomware, and its presence in mass media, are already raising these awareness levels. What we can do about this is talking more about them. To talk about them in a divulgative undertandable way that company managers can understand.

About number one, it is in our hand to improve the situation. There are plenty of cons and opportunities to improve the security community. We have to raise awareness of the good security talks. We also have to participated, contribute, and create content. If we all contribute of improving the community, pushing it to the technical part, and raising awareness of the importance that cybersecurity professionals have the technical knowledge necessary to define good security measures that are aligned with the business and that are able to talk to management and make them aware of the importance of good cybersecurity for their business.

# Improving the CRT

I'm pretty sure that the CRT has many errors, as I'm not an expert. I would like to receive your feedback about it in the form of comments here or maybe you can send me an email with your feedback to florencio.cano at gmail dot com.
