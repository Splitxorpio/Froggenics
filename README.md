# Froggenics
The ultimate fitness guide to your wellbeing!
# The problem.
Only 23 percent of American adults meet leisure-time physical activity (LTPA) guidelines, according to new research data from the Center for Disease Control's (CDC) National Center for Health Statistics, and many of these americans are not meeting the guidelines due to confusion of how to work out in a time-accordingly manner.
# The solution.
Froggenics is a completely AI-based application whose goal is to make sure you are able to reach your fitness goals physically and also maintaining mental equilibrium (which is why we have frogs!). In the case that a user is unable to find nearby facilities for fitness, we include a feature that lets users find gyms and fitness stores near their location.
# The technicality.
We used python as our main programming language. We used Flask as our main web development framework and Scikit-learn, pandas, numpy and catboost as our main ML tech stack. We used Flask because of its flexibility and simplicity which allows us to build and update apps long term. We picked Scikit-learn, pandas and numpy as our main stack for ML because that’s the industry standard for ML and it is a pretty robust stack. We used firebase as our backend database to handle all the user authentication so the user can see their schedule at later times. Lastly we choose Catboost so that our ML models are performant, accurate, and fast. 
# The Technical Aspects.
Our project is fairly complex. When the user inputs their biometrics, the flask backend sends all that data to our AI/ML model depending on their weight class and then our model then processes the data with scikit-learn. Then it feeds it to our Catboost model that has been optimized using grid search techniques for performance and it generates a 7 exercise, 7 day workout plan.
# The challenges.
<ul><h3>AI Model</h3>
<li>Making it fast [SOLVED] (Able to make it 86% faster)</li>
<li>Being able to implement AI Model output to frontend [SOLVED]</li>
</ul>
<ul><h3>Flask</h3>
<li>Creating a fault tolerant system [SOLVED]</li>
<li>Working with firebase with the first time [SOLVED]</li>
</ul>
<ul><h3>Frontend</h3>
<li>Creating a visually appealing UI [SOLVED]</li>
<li>Making the process of user input and getting output simple [SOLVED]</li>

