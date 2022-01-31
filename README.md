# We Need To Talk
MIT Code for Good '22 Data Analysis Project for We Need to Talk

[We Need to Talk](https://www.facebook.com/weneedtotalkinitiative) is a nonprofit organization that aims to provide clean, safe menstrual products and menstrual education to the Turkish population, especially those suffering from period poverty. This is their main [website](https://konusmamizgerek.org/biz-kimiz/) (as of now, it is only in Turkish however). Here is a [blog](https://assembly.malala.org/stories/menstruation-rural-turkey) written by one of the founding members, İlayda Eskitaşçıoğlu, that describes some of the central motivations behind the organization.

Our team of MIT students consists of: Bill Wu '21, Nikasha Patel '22, Nabil Khalil '22, and Andrew Gu '22.

This repo consists of our model that aims to calculate and display period poverty scores per city in Turkey as a heatmap. For our original period poverty score calculations, we obtained data from global health organizations and various other statistical sources online. The formula for calculating our period poverty score per province is:

![equation](https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;c_1&space;\times&space;di&space;&plus;&space;c_2&space;\times&space;sr&space;&plus;&space;c_3&space;\times&space;pu&space;&plus;&space;c_4&space;\times&space;hc)

where c1, c2, c3, and c4 are adjustable coefficients, di is a distress index that will be constructed from different health/education/income indices, sr is a measure proportional to the fraction of Syrian refugees per province, pu is the period unaffordability index which is based off of mostly financial factors related to menstrual product expenditure, and hc is the lack of healthcare index which determines the severity of the lack of proper healthcare services/facilities/staff. This equation will be applied to data from 81 Turkish cities to map out the period poverty severity across the country. 

This project acts as a tool for We Need to Talk to use when more data is obtained from those living in rural regions and also Syrian refugees. These populations tend to have the least access to safe and clean menstrual products. Furthermore, due to the stigma around menstrual care in Turkey, access to these products is even more difficult, especially for these at risk populations. When more data is obtained, the code in this repo can be rerun to update the model and heatmap results. 

### Add-on (as of 1/26/22):
We Need to Talk posted a survey on its social media gathering data from respondents across Turkey describing how clean, safe, and private living conditions are, as well as other important factors.

The data from this survey was incorporated into our calculations for the period poverty score, weighted by how many respondents there were per province. In the future, if many more responses are recorded and the user would want to update the scores, be sure to read the TODOs in the data_organization notebook instead of blindly re-running the cells. Please contact any one of us if you have any questions.
