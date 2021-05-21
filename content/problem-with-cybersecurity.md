title: Looking for the root cause of current cybersecurity problems
date: 2021-05-21
modified: 2021-05-21
category: Security
slug: looking-for-root-cause-current-cybersecurity-problems
author: fcano

I love Goldratt books ([The Goal](https://www.goodreads.com/book/show/113934.The_Goal), [It's Not Luck](https://www.goodreads.com/book/show/157385.It_s_Not_Luck?from_search=true&from_srp=true&qid=dQEjWkU3CN&rank=1), [The Choice](https://www.goodreads.com/book/show/4845427-the-choice?ac=1&from_search=true&qid=FWBh4M06P9&rank=3), [Critical Chain](https://www.goodreads.com/book/show/848514.Critical_Chain)) and his thinking tools. One of the thinking tools is called the Current Reality Tree (CRT). It is used when you are trying to find the root problem of a complex problem. In this case, just out of curiosity, I have tried to write a CRT for the problem of cybersecurity: Why are big and important companies having severe cybersecurity breaches? What can we do to improve this situation?

I'm not going to explain how to design a CRT. I'm going to show mine and explain it. What you need to know is that an arrow from A to B means that A causes B. We say A is a necessary condition for B to happen. If we eliminate or fix A, B will not happen.  If there is an ellipse on top of multiple arrows, it means that all the causes (A, A', A'') must be met for B to happen.

On the top of the tree we have the undesirable effects (UDEs). UDEs are what we see that is not working well and what we want to solve.

The CRT does not state any solutions, only problems (causes of the UDEs, causes of the causes of the UDEs, etc.). The last causes, those on the bottom, are the root causes. That means that if we solve the root causes, we will solve the the problems derived from them.

Goldratt's principle of Inherent Simplicity states that any complex problem, at the end, only have a few (probably one or two) root causes. That is fantastic because it means that the tree is not infinite, but it ends in only a few of causes.

This is the CRT that I wrote for the cybersecurity problem:

![Cybersecurity CRT]({filename}/images/cybersecurity_crt.jpg)

# Companies continue having severe cybersecurity incidents.

Our main and starting UDE is on the top: Companies continue having severe cybersecurity incidents. That is a fact. But, what are the reasons? For me, the first direct reason, we may like it or not, is that the companies don't have enough cybersecurity controls. If they had enough cybersecurity controls, independently of everything else, severe cybersecurity incidents won't happen. Let's continue with the causes for "Companies don't have enough cybersecurity controls".

Companies don't have enough cybersecurity controls due to one or more of these reasons:

- Companies don't know how to secure their systems.
- Companies don't want to secure their systems.
- Companies don't know they need to secure their systems.

I have not been able to think about other reasons. Let me know if you can think about another one.

# Companies don't know how to secure their systems.

One of the causes of "Companies continue having severe cybersecurity incidents" is that "Companies don't know how to secure their systems". They don't know what security controls would reduce the probability or the impact of a security threat to materialize in their company and cause severe damage. In the case of ransomware, that is the most pervasive and damaging security threat currently, this means that companies don't know which security controls they have to implement to avoid the ransomware to infect their systems and random their data.

This is not the only reason, there are two more. But while this reason is true, we will have the problem.

I see two reason why companies don't have this information:

- Companies don't have people who know how to secure their systems.
- Companies don't have people whose mission is secure their systems.

In the first case, the employees that the company has assigned to this task, protecting their systems and avoid having security breaches, don't know what security measures they have to implement.

In the second case, the companies don't even have people dedicated to that.

Let's go down following the branch of causes-effects that explain why "Companies don't have people who know how to secure their systems".

## Companies don't have people who know how to secure their systems.

Why people that are dedicated to security don't know which security measures can be implemented to reduce the risk of a security breach to acceptable levels? I know that in many cases these professional do know what to do, but the company don't let them do it. That is another branch under "Companies don't want to secure their systems", so we are not talking about this case here. Here I'm talking about not really knowing how to be protected against this.

I have thought about two reasons:

- Lack of cybersecurity people trained in technical security controls.
- People that work in cybersecurity in companies are not cybersecurity professionals.

If people that work in cybersecurity don't know the right security measures may be because they lack training or they are not really cybersecurity professionals.

The second case happens when management has heard something about security, maybe in the news or maybe because they need to comply with some regulation related to security, and they assign one IT person, that is not a security professional, to be in charge of security. This happens usually because "Management and IT is not aware of the importance of having cybersecurity professionals in the team" and that happens, in general, because there is a "Lack of management cybersecurity awareness". This is our first root cause. We will talk about it again later.

Let's continue with the other branch. Why there is a "Lack of cybersecurity people trained in technical security controls."? It is obvious that the reason is that these cybersecurity people don't get training. But, why? There are two possible reasons:

- Cybersecurity people they don't need to get training.
- Good training is expensive and there is a lack of good free security training.

"Cybersecurity people they don't need to get training" is being reinforced by the fact that "Lack of cybersecurity people trained in technical security controls". The less training, the less you think you need training. Dunning-Kruger effect in action. The CRT theory says that reinforcing loops like this are really powerful and we should focus on them when we want to find solutions.

About the second, I'm not completely sure about that. Maybe the material is there but people don't know it or don't do the effort of reading and studying it. In any case, the reason for these two cases, in my opinion, is the same. We have a "Cybersecurity community that rewards more the image than the knowledge". Some security rock stars that have been appearing in mass media have sent the message that security is cool and easy, without giving credit or raising awareness of the effort required to be a good security professional.

## Our first root causes.

By following this branch, we have arrived to two root causes. If you think that the cause-effect logic that I have used is right, you would agree with me that if we change these two root causes, we will be able to revert the UDE "Companies don’t know how to secure their systems". I will talk about solutions after having "read" the whole tree.

# Companies don’t want to secure their systems.

Are there companies that don't want to secure their systems? Yes, but they have reasons. In this part of the tree I'm going to explore that.

- Companies don't want to spend budget in cybersecurity.
- Companies do think it is ok to spend budget, but all the cybersecurity controls they know affecte negatively on the business (e.g. to its agility).

Let's start with the second, which cause is clear for me and we have already talked about it. Bad cybesecurity professionals only can think about security measures that impact negatively on the business. Thinking about security measures that are aligned with the business is difficult and it takes effort. They are not usually straighfoward in the books...you have to take what books say and transform and adapt it to a specific business. Some bad cybersecurity professional would want the the business just implements whatever they say, but the business revels against that.

Good security professionals search for the best solutions for the business. Non trivial solutions that do not affecte negatively the business or the negative impact is clearly worth it and makes sense. Bad security professional are not bad people :), they lack security training. We already have explored that and we know the root causes.

Let's explore now why companies don't want to spend money on cybersecurity. Companies do spend money in things they think they need. So, the reason is clear: the company (management) do think that cybersecurity is not necessary so they choose not to spend money nor time in cybersecurity. Management thinks so because they are not aware of the security risks. They are usually very busy, and they need people around them that explains them what they need to know in a very easy straighforward way. Here we have a reinforcing cycle again...because companies don't have people whose mission is security, management don't have people around them that talks about security and explains and make the risks visible.

There is one more reason that explains why management are not aware of cybersecurity risks: in the cases that the company do have cybersecurity people, sometimes, these cybersecurity people don't know how to talk about risks to management. Cybersecurity people is usually technical people. And we, technical people, do have in general a problem for explaining things in an easy understandable way. The reason for this is again lack of good cybersecurity training or lack of training aimed to talk about risks and how cyber risks affects companies.

# Root causes and solutions

At the end, based on the logic explained, we have that the root causes of "Companies continue having severe cybersecurity incidents" are:

1- Security community that rewards image over knowledge.
2- Lack of management cybersecurity awareness.

Let's talk about solutions.

For the second root cause, "Lack of management cybersecurity awareness", I think it is something that will improve with time. If cybersecurity is as important as we think it is, the number of security incidents will raise the awareness in a natural way. In my opinion, current security incidents due to ransomware, and its presence in mass media, are already raising these awareness levels. What we can do about this is talking more about them. To talk about them in a divulgative undertandable way that company managers can understand.

About number one, it is in hour hand to improve the situation. There are plenty of cons and opportunities to improve the security community. It is as easy as recognizing the effort of good talks and ignoring bad talks that only talk about cool hacking, instead of hard technical work. We can also contribute to the community with good open source tools that help improve cybersecurity status in general. We can also develop better open materials for everyone to consumme: a blog, a podcast, whatever.

# Improving the CRT

I would like to improve the CRT with facts that I have not taking into account, so please, don't hesitate in sending your comments.
