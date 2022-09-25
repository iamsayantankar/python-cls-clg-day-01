# python-cls-clg-day-01

#### Pattern and pascal assignment python


```txt
   *
   **
   ***
   ****
   *****
```
>```py
>  for i in range(1, 6):
>    print("*" * i)
>```


```txt
   *****
   ****
   ***
   **
   *
```
>```py
>
>  for i in range(5, 0, -1):
>      print("*" * i)
>```

```txt
       *
      **
     ***
    ****
   *****
   ****
   ***
   **
   *
```
>```py
>  for i in range(1, 6):
>      print(" " * (5 - i) + "*" * i)
>```
>```py
>  for i in range(5, 0, -1):
>      print(" " * (5 - i) + "*" * i)
>```

```txt
       *
      **
     ***
    ****
   *****
```


```txt
   *****
    ****
     ***
      **
       *
```


```txt
       *
      **
     ***
    ****
   *****
    ****
     ***
      **
       *
```


```txt
       *
      ***
     *****
    *******
   *********
```

>```py
>  for i in range(1, 6):
>      print(" " * (5 - i), end="")
>      print("*" * (i * 2 - 1))
>```

```txt
       *
      ***
     *****
    *******
   *********
    *******
     *****
      ***
       *
```


```txt
   **********
   ****  ****
   ***    ***
   **      **
   *        *
   **      **
   ***    ***
   ****  ****
   **********
```


```txt
       1
      12
     123
    1234
   12345
```


```txt
       1
      121
     12321
    1234321
   123454321
```


```txt
       1
      212
     32123
    4321234
   543212345
```


```txt
   1
   1 2
   1  3
   1   4
   12345
```


```txt
       1
      23
     345
    4567
   56789
```


```txt
       1
      232
     34543
    4567654
   567898765
```

>```py
>  for i in range(1, 6):
>      print(" " * (5 - i), end="")
>      for j in range(1, i + 1):
>          print(j + i - 1, end="")
>      for j in range(j + i - 1, i, -1):
>          print(j-1, end="")
>      print("")
>```




>```py
>  for i in range(1, 6):
>      print(" " * (5 - i), end="")
>      print("*" * (i * 2 - 1))
>```
>```py
>  for i in range(1, 10):
>      if i > 5:
>          print(" " * (5 - i), end="")
>          print("*" * (10 - i))
>      else:
>          print(" " * (5 - i) + "*" * i)
>```
>```py
>  for i in range(1, 10):
>      if i > 5:
>          print(" " * (i - 5), end="")
>          print("*" * (10 - i))
>      else:
>          print(" " * (5 - i) + "*" * i)
>```
>```py
>  for i in range(1, 10):
>      if i > 5:
?          print(" " * (i - 5), end="")
>          print("*" * (2 * (10 - i) - 1))
>      else:
>          print(" " * (5 - i), end="")
>          print("*" * (i * 2 - 1))
>```
>```py
>  for i in range(1, 10):
>      if i < 6:
>          print("*" * (6 - i), " " * (i * 2 - 1), "*" * (6 - i))
>      else:
>          print("*" * (i - 4), " " * (2 * (10 - i) - 1), "*" * (i - 4))
>```
>```py
>  for i in range(1, 10):
>      if i < 6:
>          print("*" * (6 - i), end="")
>          print(" " * (i * 2 - 2), end="")
>          print("*" * (6 - i))
>      else:
>          print("*" * (i - 4), end="")
>          print(" " * (2 * (10 - i) - 2), end="")
>          print("*" * (i - 4))
>```
>```py
>  for i in range(1, 6):
>      print(" " * (5 - i), end="")
>      for j in range(1, i + 1):
>          print(j, end="")
>      print("")
>```
>```py
>  for i in range(1, 6):
>      print(" " * (5 - i), end="")
>      for j in range(1, i + 1):
>          print(j, end="")
>      for j in range(i - 1, 0, -1):
>          print(j, end="")
>      print("")
>```
>```py
>  for i in range(1, 6):
>      print(" " * (5 - i), end="")
>      for j in range(i, 0, -1):
>          print(j, end="")
>      for j in range(1 + 1, i + 1):
>          print(j, end="")
>      print("")
>```
>```py
>  for i in range(1, 6):
>      if i == 1:
>          print(i)
>      elif i < 5:
>          print("1", end="")
>          print(" " * (i - 1), end="")
>          print(i)
>      else:
>          for j in range(1, 6):
>              print(j, end="")
>          print("")
>```
>```py
>  for i in range(1, 6):
>      print(" " * (5 - i), end="")
>      for j in range(1, i + 1):
>          print(j + i - 1, end="")
>      print("")
>```

