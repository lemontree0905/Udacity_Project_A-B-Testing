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
We first calculate the number of pageviews needed in order to power the experiment appropriately. I will NOT use the Bonferroni correction during my analysis phase. 

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
| Click-through-probability | -0.0013 | 0.0013 | -0.0001 | Pass

* For population size metrics, we first calculate the standard error with binomial with probability 0.5, that is   
<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;SE&space;=&space;\sqrt{0.5(1-0.5)/(N_{exp}&plus;N_{cont})}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;SE&space;=&space;\sqrt{0.5(1-0.5)/(N_{exp}&plus;N_{cont})}" title="\small SE = \sqrt{0.5(1-0.5)/(N_{exp}+N_{cont})}" /></a>.</p>
Then we check whether the observed value falls into the confidence interval the confidence interval around 0.5
<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;[0.5-1.96*SE,0.5&plus;1.96*SE]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;[0.5-1.96*SE,0.5&plus;1.96*SE]" title="\small [0.5-1.96*SE,0.5+1.96*SE]" /></a>.</p>

* For any other type of metric, we should construct a confidence interval for a difference in proportions. This is how it is done. We first calculate the pooled probability
<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;P_{pool}=\frac{X_{exp}&plus;X_{cont}}{N_{exp}&plus;N_{cont}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;P_{pool}=\frac{X_{exp}&plus;X_{cont}}{N_{exp}&plus;N_{cont}}" title="\small P_{pool}=\frac{X_{exp}+X_{cont}}{N_{exp}+N_{cont}}" /></a></p>.

Then we calculate the pooled standard error

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;SE_{pool}=\sqrt{P_{pool}(1-P_{pool})*(1/N_{exp}&plus;1/N_{cont})}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;SE_{pool}=\sqrt{P_{pool}(1-P_{pool})*(1/N_{exp}&plus;1/N_{cont})}" title="\small SE_{pool}=\sqrt{P_{pool}(1-P_{pool})*(1/N_{exp}+1/N_{cont})}" /></a></p>

If the true difference d between click-through-probability in the experiments and controls is zero, then we would expect that d follows a normal distribution with mean 0 and standard deviation SE. Then if the observed value d is large than 1.96SE or less than -1.96SE, then we could conclude that the difference represents a statistically significant difference. Otherwise the sanity check passes.

### Result Analysis
#### Effect Size Tests
For each of your evaluation metrics, we give a 95% confidence interval around the difference between the experiment and control groups.

A metric is statistically significant if the confidence interval does not include 0 (that is, you can be confident there was a change), and it is practically significant if the confidence interval does not include the practical significance boundary (that is, you can be confident there is a change that matters to the business.)

One should also notice that the given spreadsheet lists pageviews and clicks for 39 days, while it only lists enrollments and payments for 23 days.

|Evaluation Metric| Lower Bound | Upper Bound| Statistically Significant | Practically Significant
| --- | --- |--- |--- |--- |
|Gross conversion | -0.0291 | -0.0120 | YES | YES
|Net conversion |	-0.0116 | 0.0019  | NO | NO

#### Sign Tests
For each evaluation metric, we also do a sign test using the day-by-day data, and report the p-value of the sign test and whether the result is statistically significant.The calculation using this online calculator: https://www.graphpad.com/quickcalcs/binomial1.cfm

|Evaluation Metric| P-value | Statistically Significant 
| --- | --- |--- 
|Gross conversion | 0.0026 | YES |
|Net conversion |	0.6776 |  NO

#### Summary
I didn't use the Bonferroni correction.The results from effect size hypothesis tests are in consistent with those from sign tests.

#### Recommendation
We can see that the number of frustrated students who left the free trial has redueced while the number of students to continue past the free trial and eventually complete the course is unaffected. Therefore the hypothesis holds true, whick means this could help Udacity  improve the overall student experience and improve coaches' capacity to support students who are likely to complete the course. Therefore I will recommend launch the change.

