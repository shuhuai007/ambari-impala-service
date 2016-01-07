#An Ambari Service for Impala


##To download the Impala service folder, run below    


```
VERSION=`hdp-select status hadoop-client | sed 's/hadoop-client - \([0-9]\.[0-9]\).*/\1/'`
sudo git clone https://github.com/shuhuai007/ambari-impala-service.git /var/lib/ambari-server/resources/stacks/HDP/$VERSION/services/IMPALA        
```

##Restart Ambari
\#sandbox  
service ambari restart

\#non sandbox  
sudo service ambari-server restart