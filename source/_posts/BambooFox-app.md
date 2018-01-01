---
title: BambooFox-app
date: 2017-12-31 18:38:03
tags:
---

## Solution

1. 將apk放去 http://www.javadecompilers.com/apk decompile

2. 睇番個目錄見到有個folder叫 appinventor , 好似幾有趣 , lets see~

<img src="img1.png"/>

3. 最後係 \appinventor\ai_ss8651twtw\BambooFox\Screen1.java 搵到
``` java
public Object Button1$Click() {
	runtime.setThisForm();
    if (runtime.callYailPrimitive(Scheme.numGEq, LList.list2(runtime.lookupGlobalVarInCurrentFormEnvironment(Lit3, runtime.$Stthe$Mnnull$Mnvalue$St), Lit21), Lit22, ">=") != Boolean.FALSE) {
    	runtime.setAndCoerceProperty$Ex(Lit19, Lit23, Boolean.FALSE, Lit24);
        runtime.setAndCoerceProperty$Ex(Lit19, Lit16, "QkFNQk9PRk9Ye2phVmFfNFBQX2k1X2VhU3lfdDBfRDNjMG1waTFlfQ==", Lit9);
        return runtime.callComponentMethod(Lit25, Lit26, LList.list1("Flag in somewhere"), Lit27);
    }
    runtime.callComponentMethod(Lit25, Lit26, LList.list1("Try harder!!!"), Lit28);
    return runtime.addGlobalVarToCurrentFormEnvironment(Lit3, runtime.callYailPrimitive(AddOp.$Pl, LList.list2(runtime.lookupGlobalVarInCurrentFormEnvironment(Lit3, runtime.$Stthe$Mnnull$Mnvalue$St), Lit29), Lit30, "+"));
}```

4.
``` python
import base64
print base64.b64decode("QkFNQk9PRk9Ye2phVmFfNFBQX2k1X2VhU3lfdDBfRDNjMG1waTFlfQ==")
```

## Flag
```
BAMBOOFOX{jaVa_4PP_i5_eaSy_t0_D3c0mpi1e}
```