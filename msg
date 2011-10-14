#!/bin/bash

conf_dir="$HOME/.msg"
if [[ ! -d $conf_dir ]]; then
    mkdir $conf_dir
fi
num_file="$conf_dir/numbers"
login_file="$conf_dir/login"
login=$(cat $login_file)
unum=$(echo $login | awk -F ',' '{print $1}')
pin=$(echo $login | awk -F ',' '{print $2}')
serv=$(echo $login | awk -F ',' '{print $3}')

function add_number {
    echo "$1,$2" >> $num_file
    echo "Number added."
}

function send_msg {
    numtest='^[[:digit:]]+$'
    if [[ "$1" =~ $numtest ]]; then
        num=$1
    else
        num=$(cat $num_file | grep "$1" | awk -F ',' '{print $2}')
    fi
    shift
    msg=$(echo "$@" | sed 's/\ /%20/g' | sed "s/'/%27/g")
    url="http://cabbagetexter.com/send.php?u=$unum&p=$pin&s=$serv&d=$num&m=$msg"
    ans=$(wget -qO - $url)
    case $ans in
        -1  )   echo "Invalid login. Message not sent." ;;
        -2  )   echo "Could not log in to network website. Message not sent." ;;
        -5  )   echo "Problem with network website. Message not sent." ;;
        ""  )   echo "No message specified. Message not sent." ;;
        *   )   echo "Message sent. $ans messages left."
    esac
}

function set_login {
    echo "$1,$2,$3" > $login_file
    echo "Login set."
}

function empty {
    echo "" > $num_file
    echo "Contact book cleared."
}

function view_contacts {
    cat $num_file
}

function gui {
    if [[ $(which zenity 2>/dev/null) ]]; then
        send_msg $(zenity --entry --text='Enter the number or name of the recipient folowed by your message.')
    fi
}

case "$1" in
    "add"       )   add_number "$2" "$3" ;;
    "login"     )   set_login "$2" "$3" "$4" ;;
    "clear"     )   empty ;;
    "contacts"  )   view_contacts ;;
    ""          )   gui ;;
    *           )   send_msg "$@"
esac    
