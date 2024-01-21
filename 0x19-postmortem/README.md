# Postmortem: Database Connection Failure on January 15, 2024

## Issue Summary

On January 15, 2024, from 10:15 AM to 10:45 AM (UTC+02:00), our web application experienced a database connection failure that affected 35% of our users. The users who were affected could not access their data, create new records, or update existing ones. The root cause of the issue was a misconfigured firewall rule that blocked the traffic between the web server and the database server.

## Timeline

- 10:15 AM: The issue was detected by our monitoring system, which alerted the on-call engineer via email and SMS.
- 10:17 AM: The on-call engineer acknowledged the alert and started investigating the issue. He checked the web server logs and saw a lot of errors related to database connection timeouts.
- 10:20 AM: The on-call engineer tried to connect to the database server from the web server using a command-line tool, but failed. He suspected that there was a network issue between the two servers.
- 10:22 AM: The on-call engineer logged into the firewall console and saw that there was a new rule that was added recently, which denied all traffic from the web server to the database server. He did not know who added the rule or why.
- 10:25 AM: The on-call engineer contacted the network team and asked them to check the firewall rule. The network team confirmed that the rule was added by mistake during a routine maintenance and apologized for the error.
- 10:30 AM: The network team deleted the firewall rule and restored the connectivity between the web server and the database server.
- 10:35 AM: The on-call engineer verified that the web application was working normally and that the users could access their data again. He updated the monitoring system and closed the alert.
- 10:45 AM: The on-call engineer wrote a brief summary of the issue and sent it to the engineering manager and the customer support team.

## Root Cause and Resolution

The root cause of the issue was a misconfigured firewall rule that blocked the traffic between the web server and the database server. The firewall rule was added by the network team during a routine maintenance, but they did not test it properly or communicate it to the other teams. The issue was resolved by deleting the firewall rule and restoring the connectivity between the web server and the database server.

## Corrective and Preventive Measures

To prevent this issue from happening again, we propose the following actions:

- Implement a change management process for the firewall configuration, which requires approval from the engineering manager and the network team before applying any changes.
- Add automated tests for the firewall rules, which verify that the web server can communicate with the database server and other critical services.
- Improve the communication and coordination between the network team and the engineering team, especially during maintenance windows.
- Provide training and documentation for the network team on how to configure and troubleshoot the firewall.
- Review and audit the firewall rules regularly and remove any unnecessary or outdated ones.

