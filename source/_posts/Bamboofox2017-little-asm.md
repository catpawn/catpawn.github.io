---
title: Bamboofox2017-little-asm
date: 2018-01-01 16:58:10
tags:
---

## Question

### Binary
[little-asm-221bc5c8651806d8a039d5ff2a68bc5c7d9e3a20](little-asm-221bc5c8651806d8a039d5ff2a68bc5c7d9e3a20)


## Solution

第一步都係扔入ida decompile個main睇睇咩料先!

``` c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int result; // eax@6
  __int64 v4; // rsi@10
  int i; // [sp+4h] [bp-3Ch]@1
  int j; // [sp+8h] [bp-38h]@4
  int v7; // [sp+Ch] [bp-34h]@1
  char s[8]; // [sp+10h] [bp-30h]@1
  __int64 v9; // [sp+18h] [bp-28h]@1
  __int64 v10; // [sp+20h] [bp-20h]@1
  __int64 v11; // [sp+28h] [bp-18h]@1
  __int64 v12; // [sp+30h] [bp-10h]@1
  __int64 v13; // [sp+38h] [bp-8h]@1

  v13 = *MK_FP(__FS__, 40LL);
  puts("Input magic string:");
  *(_QWORD *)s = 0LL;
  v9 = 0LL;
  v10 = 0LL;
  v11 = 0LL;
  v12 = 0LL;
  _isoc99_scanf("%36s", s);
  v7 = strlen(s);
  for ( i = 0; i < v7; ++i )
    s[i] ^= 0xDCu;
  for ( j = 0; j < v7; ++j )
  {
    if ( s[j] != ans[j] )
    {
      puts("Are you sure you read asm?");
      result = 0;
      goto LABEL_10;
    }
  }
  puts("Wooow you got it!");
  result = 0;
LABEL_10:
  v4 = *MK_FP(__FS__, 40LL) ^ v13;
  return result;
}
```

我地可以見到個program首先會讀36位既input
``` c
_isoc99_scanf("%36s", s);
```

然後做同0xDC做xor
``` c
for ( i = 0; i < v7; ++i )
	s[i] ^= 0xDCu;
```

最後同 ans 逐個byte做對比
``` c
for ( j = 0; j < v7; ++j )
  {
    if ( s[j] != ans[j] )
    {
      puts("Are you sure you read asm?");
      result = 0;
      goto LABEL_10;
    }
}
```

所以我地可以直接睇下ans save住d咩
![](img1.png)

然後export to hex 睇下咩黎
![](img2.png)

咁就可以寫條script解番條flag出黎 :D

``` python
hex(0x9e9d919e93939a9384a785eca983e88e9983bd839becec98839de991838eefbd98b9aea1 ^ 0xdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdc)[2:].rstrip("L").decode('hex')
```


### Flag
BAMBOOFOX{Y0u_4RE_a_G00D_A5M_R3aDer}