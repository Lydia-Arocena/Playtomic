# Playtomic
![picture](Images/plytomic_pic.png)

# Objetive:
This technical test aims to answer to some hypothetical questions that could be asked by different Playtomic stakeholders.
# Repo Structure:
- Data: folder with the csv and both jsons provided.
- Images: folder that contains the cover picture.
- src: folder that contains a .py file with fuctions I have used for my data analysis.
- config.py: file with some python objects I have import to my Notebook.
- A Jupyter Notebook called "Data_exploration" where I have carried out my test.
# Conclusions:
- **How many matches have been played overall?**

    70,985 matches have been played.

- **Where are we present and how are we performing? What can we expect for the upcoming months?**

    Playtomic is mainly present in Spain but it has also presence in other 4 countries: Italy, Denmark, Belgium and Mexico. 

    It could be said that Playtomic is performing reallly well:
    - As explained in the first graph in the Notebook, we can see that the ratio of cancellation per country is quite low, except in Italy.
    - In the second graph of the above mention Notebook, taking into account our data is from 25/03/2021 until 15/01/2022, we can see how the number of matches played have been sharply increasingly, specially, from October onwards. 

    Therefore, we could expect for the upcoming months an increase of the number of played match with a low ratio of cancellation. 

- **How many active clubs do we have each month?** 

    The number of clubs per month has increased from April 2021 to January 2022:
    - April 2021: 1 club.
    - May 2021: 0 clubs.
    - June 2021: 1 club.
    - July 2021: 2 clubs.
    - August 2021: 1 club.
    - September 2021: 8 clubs.
    - November 2021: 9 clubs.
    - December 2021: 9 clubs.
    - January 2022: 9 clubs.

- **How are they performing?**

    "Pádel Club" is the club that is performing the best by bar followed by "Club El Padelito" and "Pádel Élito Top Club".

-  **Can we see some relevant trends? Do we have newcomers?**

    We can see how the number of clubs is progressively increasing. For example, in November we have a newcomer ("World of Padel") which is doing great in terms of number of matches played in its club.

- **How many matches have been published?**

    93,723 matches were published.

- **How many of these were canceled and why?**

    22,738 matches were canceled out the total. According to the following json called "Matches history", the main reasons for cancellating are: 
    - Missing players.
    - No availability.
    - Canceled by admin.

- **Can you provide me with a list of users registered to my matches?**

    For example, let's say that the *Pádel Club manager* ask us for a list of users registered to its matches: (*see the whole list in Jupyter Notebook*).

- **How many users are coming back to my club?**

    If we stick to the previous example and we are still referring to the Pádel Club manager: we could tell him/her that there are 3,264 users that have come back to the club.

- **Who are the my most valuable clients?**

    I would say that their most valuable clients are CMMER and AREEPG as they are the most frequent clients in this club.

- **What is my occupation rate?**

    At first glance, I wouldn't know which is a club occupation rate as I don't data related to the number of total courts in order to compare it with the occupied courts.


# Libraries:
- [Pandas](https://pandas.pydata.org/docs/)
- [Json](https://docs.python.org/3/library/json.html)
- [Seaborn](https://seaborn.pydata.org/)
- [Plotly Express](https://plotly.com/python/plotly-express/)


# Time spent:
This technical test has been made between yesterday evening (27/01/2022) an today morning (28/01/2022).

