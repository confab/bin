#! /bin/bash
cd "$(dirname "$1")"
device_path=/media/5CCB-398D

while [[ -n $1 ]]
    do
    if [[ ! -e $device_path ]]
    then
        echo "Mp3 player not found."
        exit 1
    fi

    filetype=$(echo $1 | awk -F . '{print $NF}')
    filename=$(basename "$1" .$filetype)

    if [[ $filetype == "ogg" ]]
    then
        title=$(tagtool --dump "$1" | grep "\<title\> \+" | cut -d \  -f2- | cut -d \" -f2)
        album=$(tagtool --dump "$1" | grep "\<album\> \+" | cut -d \  -f2- | cut -d \" -f2)
        artist=$(tagtool --dump "$1" | grep "\<artist\> \+" | cut -d \  -f2- | cut -d \" -f2)
    else    # if not OGG, then MP3; WMA not catered for yet.
        title=$(tagtool --dump "$1" | grep --context=1 TIT2 | tail -n 1)
        album=$(tagtool --dump "$1" | grep --context=1 TALB | tail -n 1)
        for tag in "TPE1" "TPE2" "TPE3" "TPE4"
        do
            artist=$(tagtool --dump "$1" | grep --context=1 "$tag" | tail -n 1)
            if [[ -n $artist ]]
            then break
            fi
        done
    fi
    # If all else fails, derive details from file path.
    if [[ -z $title ]]
    then title=$filename
    fi
    if [[ -z $album ]]
    then album="$(pwd | awk -F / '{print $NF}')"
    fi
    if [[ -z $artist ]]
    then artist="$(pwd $1 | awk -F / '{print $(NF-1)}')"
    fi

    dest=$(echo "$device_path/$artist/$album" | sed -e 's/\t//g')
    if [[ ! -e $dest ]]
    then 
        echo "$dest does not exist; creating."
        mkdir -p "$dest"
    fi

    if [[ $filetype != "mp3" && $filetype != "wma" ]]
    then echo "Converting $(basename "$1")"; ffmpeg -i "$(basename "$1")" "$dest/$title.mp3"
    else echo "Copying $(basename "$1")"; cp -R "$(basename "$1")" "$dest"
    fi
    shift
done
echo "Done."
