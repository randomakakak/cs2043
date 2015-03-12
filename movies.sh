#! /usr/bin/env bash

 curl https://web.archive.org/web/20140301052344/http://www.movies.com/rss-feeds/top-ten-box-office-rss | 
awk -F\" '{ for(i=1;i<NF;i++) if ($(i+1) ~ /RSS/) print $i }'