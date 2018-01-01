---
title: Bamboofox2017-little-asm-revenge
date: 2018-01-01 17:12:48
tags:
---

## Question
[little-asm-revenge](little-asm-revenge)

## Solution
扔入ida睇下個main咩料先

``` c
__int64 __fastcall main(__int64 a1, char **a2, char **a3)
{
  __int64 result; // rax@9
  __int64 v4; // rsi@13
  unsigned int i; // [sp+0h] [bp-E0h]@1
  int j; // [sp+4h] [bp-DCh]@4
  int k; // [sp+8h] [bp-D8h]@7
  int v8; // [sp+Ch] [bp-D4h]@1
  int v9[40]; // [sp+10h] [bp-D0h]@4
  char s[8]; // [sp+B0h] [bp-30h]@1
  __int64 v11; // [sp+B8h] [bp-28h]@1
  __int64 v12; // [sp+C0h] [bp-20h]@1
  __int64 v13; // [sp+C8h] [bp-18h]@1
  __int64 v14; // [sp+D0h] [bp-10h]@1
  __int64 v15; // [sp+D8h] [bp-8h]@1

  v15 = *MK_FP(__FS__, 40LL);
  puts("Input magic string:");
  *(_QWORD *)s = 0LL;
  v11 = 0LL;
  v12 = 0LL;
  v13 = 0LL;
  v14 = 0LL;
  _isoc99_scanf("%38s", s);
  v8 = strlen(s);
  for ( i = 0; (signed int)i < v8; ++i )
    s[i] ^= sub_7F4(i);
  memset(v9, 0, sizeof(v9));
  for ( j = 0; j < v8; ++j )
    v9[j] = sub_7B0((unsigned int)s[j]);
  for ( k = 0; k < v8; ++k )
  {
    if ( v9[k] != dword_201040[k] )
    {
      puts("Are you sure you read asm?");
      result = 0LL;
      goto LABEL_13;
    }
  }
  puts("Wooow you got it!");
  result = 0LL;
LABEL_13:
  v4 = *MK_FP(__FS__, 40LL) ^ v15;
  return result;
}
```

首先個program會讀38位Input
``` c
_isoc99_scanf("%38s", s);
```

然後會用 sub_7F4 呢個function提供既return value做xor
``` c
for ( i = 0; (signed int)i < v8; ++i )
    s[i] ^= sub_7F4(i);
```

然後會將xor完既結果逐個入落去sub_7B0做運算 , 然後將return value逐個扔番入v9
``` c
for ( j = 0; j < v8; ++j )
    v9[j] = sub_7B0((unsigned int)s[j]);
```

最後會將v9 同 dword_201040逐個byte做對比
``` c
for ( k = 0; k < v8; ++k )
  {
    if ( v9[k] != dword_201040[k] )
    {
      puts("Are you sure you read asm?");
      result = 0LL;
      goto LABEL_13;
    }
  }
```

咁既話即係首先我地要知道 dword_201040 放緊D乜
![](img1.png)

同埋sub_7F4 , sub_7B0 做緊乜
``` c
__int64 __fastcall sub_7F4(int a1)
{
  int v2; // [sp+Ch] [bp-8h]@1
  signed int i; // [sp+10h] [bp-4h]@1

  v2 = a1;
  for ( i = 0; i <= 6; ++i )
  {
    if ( i & 1 )
      v2 ^= 1 << i;
    else
      v2 |= 1 << i;
  }
  return (unsigned __int8)v2;
}
```

``` c
__int64 __fastcall sub_7B0(int a1)
{
  int v2; // [sp+Ch] [bp-8h]@1
  int i; // [sp+10h] [bp-4h]@1

  v2 = 1;
  for ( i = 0; i < dword_201024; ++i )
    v2 = a1 * v2 % dword_201020;
  return (unsigned int)v2;
}
```

原來仲有個 dword_201024
``` asm
.data:0000000000201024 dword_201024    dd 7                    ; DATA XREF: sub_7B0:loc_7E4r
```

咁就應該齊料寫個program去爆番條flag出黎
``` c++
#include "stdafx.h"

int sub_7F4(int a1);
int sub_7B0(int a1);

int ida_chars2[] =
{
	0x19c, 0x169, 0x30, 0x1d6, 0x30, 0x30, 0x199,0x6a, 0x157, 0x0c2,
	0x10a, 0x155, 0x150, 0x107, 0x37, 0x12e, 0x22, 0x0f1, 0x1ae,
	0x151, 0x0f1, 0x1a, 0x1a5, 0x1ae, 0x0c9, 0x12c, 0x1, 0x166,
	0x12c, 0x0cb, 0x30, 0x107, 0x166, 0x1b4, 0x1ae, 0x14c, 0x46, 0x00, 0x00, 0x00
};

int main()
{
	int size = 40;
	int index = 0;
	while (1) {
		for (int i = 0x30; i < 0x126; i++) {
			int flag = i;
			flag ^= sub_7F4(index);
			if (sub_7B0(flag) == ida_chars2[index]) {
				printf("%c", i);
				index++;
			}
			if (index == 38)
				break;
		}
	}
	getchar();
    return 0;
}

int sub_7B0(int a1) {
	int v2 = 1;
	for (int i = 0; i < 7; ++i) {
		v2 = a1 * v2 % 0x1e1;
	}
	return v2;
}

int sub_7F4(int a1) {
	int v2;
	v2 = a1;

	for (int i = 0; i <= 6; ++i) {
		if (i & 1)
			v2 ^= 1 << i;
		else
			v2 |= 1 << i;
	}
	return v2;
}
```


## Flag
BAMBOOFOX{Th4t_1S_s0_eAsY_tO_rEverS3}