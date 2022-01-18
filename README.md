# We Need To Talk
MIT Code for Good '22 Data Analysis Project for We Need to Talk

[We Need to Talk](https://www.facebook.com/weneedtotalkinitiative) is a nonprofit organization that aims to provide clean, safe menstrual products and menstrual education to the Turkish population, especially those suffering from period poverty. This is their main [website](https://konusmamizgerek.org/biz-kimiz/) (as of now, it is only in Turkish however). Here is a [blog](https://assembly.malala.org/stories/menstruation-rural-turkey) written by one of the founding members, İlayda Eskitaşçıoğlu.

Our team of MIT students consists of: Bill Wu '21, Nikasha Patel '22, Nabil Khalil '22, and Andrew Gu '22.

This repo consists of our model (WIP) that aims to calculate and display period poverty scores per city in Turkey as a heatmap. The data sources and main model formula are rough so far. We scrounged up what data we could find on the internet from global health organizations and various other statistical sources. The formula for calculating our period poverty score is:

![equation](https://latex.codecogs.com/gif.image?\dpi{110}&space;c_1&space;\times&space;w&space;&plus;&space;c_2&space;\times&space;\frac{p}{i}&space;&plus;&space;c_3&space;\times&space;r&space;\times&space;c)

This project is more a tool for We Need to Talk to use once more data is obtained from rural regions and also from Syrian refugees. These populations tend to have the least access to safe and clean menstrual products. Furthermore, due to the stigma around menstrual care in Turkey, access to these products is even more difficult, especially for these at risk populations. When more data is obtained, the code in this repo can be rerun to update model and heatmap results. 

TODO: step by step procedure to run the code for generating the heatmap, also procedure for changing spreadsheet columns to fill in correct data + adding more factors to model
