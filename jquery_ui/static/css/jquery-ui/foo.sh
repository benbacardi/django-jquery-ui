#!/bin/bash

rm ._*
rm jquery.ui.theme.css
DIR=${PWD##*/}
curl -o jquery-ui.css "http://code.jquery.com/ui/1.9.2/themes/$DIR/jquery-ui.css"
