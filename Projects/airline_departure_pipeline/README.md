**Challenges & Observations**

Cluster config, Date & time fields gave me a lot of unforseen issues
* Cluster config - this project is utilizing Azure free computes - I knew that I should have use Job cluster for my pipeline but I decided to use my all purpose "free" cluster. A job stalled and the compute was stuck in idle mode which disrupted my databricks UI - on the compute page, job cluster page, notebooks were also locked. 

  * Fix: First, looked into the issue to find out if I was being billed - my virtual computes in Azure was not in use so I was clear. Secondly I tried logging out and refreshing cache & history in browser - which didnt work. I gave it some time and still no ressolve. I then installed databricks CLI on my local terminal - there I deleted my cluster - tried to create other clusters that would work to attempt to rest any handshake type configs databricks may have still had open. The clusters I created never started (as resources were unavailable). After all this I tried used another desktop and found that I had no obstructions and it was indeed a browser issue. I reset the graphics acceleration option in chrome (thank you open AI).

* Date Format - the date format of the sourced data was not in correct format for databricks in bronze layer I added schem structure of datetype and it worked teh first few runs but almost out of the blue it gave errors. 
  * Fix - I brought the field in as a stringtype and then I reformatted it to appropriate layout.

* Timestamp Format - I had created several date-time tiestamps by concatenating my date field with other time stamps, format "YYYY-mm-ddHH:mm". This worked and I hadn't gotten an issue until after I ran into issues with my cluster idling and creating a new cluster. I'm not sure for the reason but it may have been due to changes in the runtime version, that made this format now invalid. Also it may have just been that this error was just missed until then. I then ran into another issue after ressolving the format was that some ofmy time values were in incorrect 24hr format where midnight came in as '24' instead of '00'. 
  * Fix: used concat_ws and added a space bewteen my date and time, I also didnt add seconds (though this had no impact on the fix). I also added a regex_replace helper function (not singled to time), that helped me change those 24's to 00's. As it relates to the dates related to the 24s I assume they were correct and did no additional enhancements.

These issues though seemingly small was the greatest hurdles for me in creating this abstract pipeline. 

Subscription Tier also expired in Azure & Databricks so upon Upgrading I was swapped to a premium worspace .... and due to the sku that was confgiured in the trial version i was not able to downgrade to standard account. I had to delete my workspace and start over .. thankfully all my code already existed in github. 

I have not yet created any DABs so I did lose my initial pipeline setup. 