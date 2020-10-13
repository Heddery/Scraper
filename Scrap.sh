#!/bin/bash



fileName="config.json"

Username=$(sed -e 's/^"//' -e 's/"$//' <<< $(jq .Username $fileName))
Password=$(sed -e 's/^"//' -e 's/"$//' <<< $(jq .Password $fileName))
Path=$(sed -e 's/^"//' -e 's/"$//' <<< $(jq .Path $fileName))

python pluralsight.py $Path

while  read -r Course && read -r Link <&3; 
do
   ## take some action on $line
  echo $Course" ---- "$Link


  youtube-dl -o "~/Videos/Tutorials/PluralSight/Paths/$Course/%(playlist)s/%(chapter_number)s. %(chapter)s/%(playlist_index)s. %(title)s.%(ext)s" --username $Username --password $Password --restrict-filenames --sleep-interval 60 $Link

done < "Course.txt" 3<"links.txt"



rm Course.txt links.txt