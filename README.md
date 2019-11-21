# Udacity_Project_A-B-Testing

## Experiment Overview
At the time of this experiment, Udacity courses currently have two options on the course overview page: "start free trial", and "access course materials". If the student clicks "start free trial", they will be asked to enter their credit card information, and then they will be enrolled in a free trial for the paid version of the course. After 14 days, they will automatically be charged unless they cancel first. If the student clicks "access course materials", they will be able to view the videos and take the quizzes for free, but they will not receive coaching support or a verified certificate, and they will not submit their final project for feedback.

In the experiment, Udacity tested a change where if the student clicked "start free trial", they were asked how much time they had available to devote to the course. If the student indicated 5 or more hours per week, they would be taken through the checkout process as usual. If they indicated fewer than 5 hours per week, a message would appear indicating that Udacity courses usually require a greater time commitment for successful completion, and suggesting that the student might like to access the course materials for free. At this point, the student would have the option to continue enrolling in the free trial, or access the course materials for free instead. This screenshot shows what the experiment looks like.

The hypothesis was that this might set clearer expectations for students upfront, thus reducing the number of frustrated students who left the free trial because they didn't have enough time—without significantly reducing the number of students to continue past the free trial and eventually complete the course. If this hypothesis held true, Udacity could improve the overall student experience and improve coaches' capacity to support students who are likely to complete the course.

The unit of diversion is a cookie, although if the student enrolls in the free trial, they are tracked by user-id from that point forward. The same user-id cannot enroll in the free trial twice. For users that do not enroll, their user-id is not tracked in the experiment, even if they were signed in when they visited the course overview page.

## Metric Choice
There are two types of metrics for a successful experiment: Invariant (which you don't expect to change) and evaluation metrics. 

In the given experiment, we choose the following invariant metrics:
- Number of cookies: That is, number of unique cookies to view the course overview page. (dmin=3000)
- Number of clicks: That is, number of unique cookies to click the "Start free trial" button (which happens before the free trial screener is trigger). (dmin=240)
- Click-through-probability: That is, number of unique cookies to click the "Start free trial" button divided by number of unique cookies to view the course overview page. (dmin=0.01)

and the evaluation Metrics are as follows:
- Gross conversion: That is, number of user-ids to complete checkout and enroll in the free trial divided by number of unique cookies to click the "Start free trial" button. (dmin= 0.01)
- Net conversion: That is, number of user-ids to remain enrolled past the 14-day boundary (and thus make at least one payment) divided by the number of unique cookies to click the "Start free trial" button. (dmin= 0.0075)


## Measuring Variability
For each metric selected as an evaluation metric, we estimate its standard deviation analytically. Given a sample size of 5000 cookies visiting the course overview page, the standard deviations are as follows (Recall that the standard deviation is defined as<a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;\sigma=\sqrt{p(1-p)/n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;\sigma=\sqrt{p(1-p)/n}" title="\small \sigma=\sqrt{p(1-p)/n}" /></a> with n the sample size):

|Evaluation Metric| Standard Deviation
| --- | --- |
|Gross Conversion | 0.0202
|Net Conversion |	0.0156

The analytic estimates would be comparable to the empirical variability in both case the unit of diversion is equal to the unit of analysis.

## Sizing

### Number of Samples vs. Power
We first calculate the number of pageviews needed in order to power the experiment appropriately. I will NOT use the Bonferroni correction during my analysis phase because the two metrics are not independent. 
The calculation can be done by using the online calculator:
http://www.evanmiller.org/ab-testing/sample-size.html

#### Net Conversion
* Baseline Conversion: 10.9313%
* Minimum Detectable Effect: 0.75%
* alpha: 5%
* beta: 20%
* 1 - beta: 80%
* sample size = 27,413 enrollments/group
* Number of groups = 2 (experiment and control)
* total sample size = 54,826
* pageviews = 54,826/Click-through-probability = 685,325
#### Gross Conversion
* Baseline Conversion: 20.625%
* Minimum Detectable Effect: 1%
* alpha: 5%
* beta: 20%
* 1 - beta: 80%
* sample size = 25,835 enrollments/group
* Number of groups = 2 (experiment and control)
* total sample size = 51,670 enrollments
* clicks/pageview: 3200/40000 = .08 clicks/pageview
* pageviews = 51,670/Click-through-probability = 645,875

### Duration vs. Exposure
We would divert 100% of traffic, and the experiment would take about 18 days given 40,000 page views per day.
In terms of duration, an 18-day experiment looks pretty reasonable, but 100% diversion may be scaled down depending on whether there are other experiments of interest are being performed concurrently.

## Experiment Analysis
### Sanity Checks
For each of the invariant metrics, we test it at the 95% confidence interval.

|Invariant Metric| Lower Bound | Upper Bound| Observerd | Passes
| --- | --- |--- |--- |--- |
|Number of cookies | 0.4988 | 0.5012 | 0.5006 | Pass
|Number of clicks |	0.4959 | 0.5041 | 0.5005 | Pass
| Click-through-probability | 0.0202 | 0.0202 | Pass

For population size metrics, we first calculate the standard error with binomial with probability 0.5, that is 
<a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;SE&space;=&space;\sqrt{0.5(1-0.5)/(N_{exp}&plus;N_{cont})}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;SE&space;=&space;\sqrt{0.5(1-0.5)/(N_{exp}&plus;N_{cont})}" title="\small SE = \sqrt{0.5(1-0.5)/(N_{exp}+N_{cont})}" /></a>. Then we comupute the confidence interval around 0.5, which is <a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;[0.5-1.96*SE,0.5&plus;1.96*SE]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;[0.5-1.96*SE,0.5&plus;1.96*SE]" title="\small [0.5-1.96*SE,0.5+1.96*SE]" /></a>. Finally we check whether the observed value falls into the confidence interval.



