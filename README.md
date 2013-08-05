blink
=====

Process status utility for Blinkstick. Make it executable and symlink it to bin:
~~~
chmod +x blink.py
ln -s blink.py ~/bin/blink
~~~

It will pulse white while your process is going and then light up red or green
depending on the outcome. Then you can press enter to turn it off. I use it for
processes that take a long time, like running automated tests.
~~~
blink cucumber
~~~
