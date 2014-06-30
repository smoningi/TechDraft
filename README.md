This program collects data from an applicants linkedin profile, so the applicant themselves don't have to worry about entering their information (work experience, skills, etc.) themselves.

How to run:





















**Idea (Would have implemented if we had time) - Sentiment Analysis On Users' Online Feed **
================================

This would fall under the bucket of Uniqueness Data.

We would pull as many messages we can lay our hands on from the User's Facebook profile, Twitter profile, and other profiles and run them through HP's sentiment analysis library to collect the following data:

1) Is the User Social online? - We determine this by looking at the nummber of messages over a certain time period.
   EG: If user only posted 10 messages in total to Facebook/Twitter etc withint the past 2 years, then we can generalize that the user is not that social online.


2) Personality - We can get the User's Typical Mood, whether it be Positive, or Negative, or Neutreul by running text we data scrap/collect via HP sentiment analysis.

  EG: User has 90% Negative messages and 5% neutral, and 5%  positive, we can gerneralize that the user might be suffering from depression, so interview with care.
  
  
  One Sample Sentiment Analysis:
  
 " I visited san fran today to compete at TECH DRAFT - I'm so excited and happy. BEST TIME OF MY LIFE! "
 
  Polarity

    pos: 0.8
    neg: 0.2 
    
"OMG. Life Sucks...it is terrible... I just failed in physics test. CRUEL WORLD!!!!"

Polarity

    pos: 0.1
    neg: 0.9 


**SAMPLE Text Sentiment Analysis Online: http://text-processing.com/demo/sentiment/**
  
  

