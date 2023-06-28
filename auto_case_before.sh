#!/bin/bash
forpath=har/lth/
ls $forpath | while read line
do
    file=${forpath}${line}
    echo "生成$file 的yaml文件"
    har2case $file -2y
done

cp har/lth/*.yml testcases/lth
echo "******************可执行文件生成完毕，开始执行测试用例******************"