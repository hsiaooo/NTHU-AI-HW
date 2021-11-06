# LunarLander
---
<p align="center">
  <img src="img/original.gif"  alt="Sublime's custom image"/>
</p>


<p align="center">image credit by <a href="https://gym.openai.com/envs/LunarLanderContinuous-v2/">openai.com</a></p>

## You will learn to solve problem using genetic algorithm (GA).
LunarLander is a game in Open AI Gym. In this game, the task is to navigate the lander to the landing pad. By precisely controlling the lander's main engine and side engines, which produce the vertical and horizontal thrust, the lander can land on pad safely.

A safety landing on the landing pad gets a positive reward. A safety landing outside the landing pad gets no reward. Crashing the lander yields a huge negative reward. In addition, the total fuel consumption is converted into a negative reward. In other words, your lander is expected to perform a safe, precise, and fuel-efficient maneuver to maximize the reward received.

### Problem Description
In this assignment, you are asked to optimize the control policy of the lunar lander with genetic algorithm (GA). The lunar lander continuously observes its status and the environment and pilots itself according to the control policy you provided. We have implemented a GA and testing framework for you. Your task is to design and implement the evolutionary operators and tune the parameters for GA so that GA works effectively and efficiently.

**observes**  

> For every time stamp, the lunar lander receives an observation vector which contains the following dimensions:
> * x position 
> * y position
> * x velocity 
> * y velocity
> * tilt angle
> * angular velocity
> * whether the right leg attaches to the ground (unused)


**action**
> The lunar land allows us to control the main engine and side engines. An action therefore consists of 2 dimensions, i.e., 
> * main engine power
> * side engine power
> The main engine power and side engine power each consists of a real value in [−1, 1], indicating the thrust of the engines. For the main engine power, a value < 0 stops the engine to produce thrust. For the side engine power, a negative value and a positive value refer to the left and right engine thrust, respectively.


**control policy**
> To establish a complete mapping between the observation and action spaces, a control policy must encode an action for each observation case. In other words, a control policy will be an 8192-dimensional vector (4^6 × 2), where each value is in [−1, 1]. You need to use GA to optimize the 8,192 thrust values for the lunar lander to gain as high reward as possible. 


## System Requirement 
**window 10**
```
pip install gym
pip install box2d
pip install pyglet
```

**Mac OS**
```
pip3 install gym[all]
pip3 install box2d
```

---
Reference: [LunarLand GA](https://sites.google.com/gapp.nthu.edu.tw/lunarlander-ga)


<font size=1> This site is composed by Heng-An Chen, Yi-Reui Chen, Yu-Wei Wen . Last update 2020.11.04 </font><br>
<font size=1> Computational Intelligence Lab (CI Lab), Dept. of PME, NTHU, Taiwan. </font>

<!DOCTYPE html>
<html itemscope="" itemtype="http://schema.org/WebPage" lang="en-US">
 <head>
  <meta charset="utf-8"/>
  <script nonce="PlDSnyC9Wpbidv1t4uPZIw">
   var DOCS_timing={}; DOCS_timing['sl']=new Date().getTime();
  </script>
  <script nonce="PlDSnyC9Wpbidv1t4uPZIw">
   function _DumpException(e) {throw e;}
  </script>
  <script nonce="PlDSnyC9Wpbidv1t4uPZIw">
   _docs_flag_initialData={"atari-emtpr":false,"docs-sup":"","docs-eea":false,"docs-eldi":false,"docs-ecci":false,"docs-ipmmp":true,"docs-esi":false,"docs-liap":"/logImpressions","ilcm":{"eui":"AHKXmL2l1dbdY7115XsqthttbdYLXv8snocwVzJAE5bIRtmLXEmSdreQnphN0vbTiLuDv3NQ1hn0","je":1,"sstu":1636222121570000,"si":"CJPi0bKqhPQCFQ6FIwAdxVsK5Q","gsc":null,"ei":[5752694,5706832,5739802,5754229,5713049,5732942,5736243,5740908,5729664,5745792,14101306,5707711,5748029,5735806,5749140,14101510,5740814,5753329,5720925,5711808,14101502,5742462,5713207,14101534,5738509,5704621,5747261,5703839,5739897,5734954,5720060,5714628,5738529,5708870,5747741,5706836,5734571,5741775,5737337,5745622,5743124,5714550,14101530],"crc":0,"cvi":[]},"docs-ccdil":false,"docs-eil":true,"docs-eoi":false,"info_params":{},"atari-jefp":"/_/view/jserror","docs-jern":"view","atari-rhpp":"/_/view"}; _docs_flag_cek= null ; if (window['DOCS_timing']) {DOCS_timing['ifdld']=new Date().getTime();}
  </script>
  <meta content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no" name="viewport"/>
  <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
  <meta content="origin" name="referrer"/>
  <link href="https://ssl.gstatic.com/atari/images/public/favicon.ico" rel="icon"/>
  <meta content="LunarLander GA" property="og:title"/>
  <meta content="website" property="og:type"/>
  <meta content="https://sites.google.com/gapp.nthu.edu.tw/lunarlander-ga" property="og:url"/>
  <meta content="
Image credit: Gym (openai.com) " property="og:description"/>
  <meta content="LunarLander GA" itemprop="name"/>
  <meta content="
Image credit: Gym (openai.com) " itemprop="description"/>
  <meta content="https://sites.google.com/gapp.nthu.edu.tw/lunarlander-ga" itemprop="url"/>
  <meta content="https://lh4.googleusercontent.com/PfrVybI-4e1TV7XWqNIddQobs1duxwU1F5yDsrll8KVUE0g2XF8rD2Ge6cLRzMmqyRdK_M_mAYrRGijz0Htm0CIu4w4V6dXoIPtngoCAYLmkggpv1kdKgKcfT3m-IcIlPQ=w1280" itemprop="thumbnailUrl"/>
  <meta content="https://lh4.googleusercontent.com/PfrVybI-4e1TV7XWqNIddQobs1duxwU1F5yDsrll8KVUE0g2XF8rD2Ge6cLRzMmqyRdK_M_mAYrRGijz0Htm0CIu4w4V6dXoIPtngoCAYLmkggpv1kdKgKcfT3m-IcIlPQ=w1280" itemprop="image"/>
  <meta content="https://lh4.googleusercontent.com/PfrVybI-4e1TV7XWqNIddQobs1duxwU1F5yDsrll8KVUE0g2XF8rD2Ge6cLRzMmqyRdK_M_mAYrRGijz0Htm0CIu4w4V6dXoIPtngoCAYLmkggpv1kdKgKcfT3m-IcIlPQ=w1280" itemprop="imageUrl"/>
  <meta content="https://lh4.googleusercontent.com/PfrVybI-4e1TV7XWqNIddQobs1duxwU1F5yDsrll8KVUE0g2XF8rD2Ge6cLRzMmqyRdK_M_mAYrRGijz0Htm0CIu4w4V6dXoIPtngoCAYLmkggpv1kdKgKcfT3m-IcIlPQ=w1280" property="og:image"/>
  <link href="https://fonts.googleapis.com/css?family=Lato%3A300%2C300italic%2C400%2C400italic%2C700%2C700italic&amp;display=swap" nonce="8mzp1G22vLR+L+rvQVdG3w" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css?family=Google+Sans:400,500|Roboto:300,400,500,700|Source+Code+Pro:400,700&amp;display=swap" nonce="8mzp1G22vLR+L+rvQVdG3w" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css?family=Lato%3Ai%2Cbi%2C700%2C400%2C300%7CSource%20Code%20Pro%3Ai%2Cbi%2C700%2C400%7CPT%20Sans%3Ai%2Cbi%2C700%2C400&amp;display=swap" nonce="8mzp1G22vLR+L+rvQVdG3w" rel="stylesheet"/>
  <style nonce="8mzp1G22vLR+L+rvQVdG3w">
   @media only screen and (max-width: 479px){.OGiC0d{font-size: 15.0pt;}}@media only screen and (min-width: 480px) and (max-width: 767px){.OGiC0d{font-size: 15.0pt;}}@media only screen and (min-width: 768px) and (max-width: 1279px){.OGiC0d{font-size: 15.0pt;}}@media only screen and (min-width: 1280px){.OGiC0d{font-size: 15.0pt;}}@media only screen and (max-width: 479px){.puwcIf{font-size: 20.0pt;}}@media only screen and (min-width: 480px) and (max-width: 767px){.puwcIf{font-size: 22.0pt;}}@media only screen and (min-width: 768px) and (max-width: 1279px){.puwcIf{font-size: 24.0pt;}}@media only screen and (min-width: 1280px){.puwcIf{font-size: 24.0pt;}}@media only screen and (max-width: 479px){.RijTuc{font-size: 25.0pt;}}@media only screen and (min-width: 480px) and (max-width: 767px){.RijTuc{font-size: 30.0pt;}}@media only screen and (min-width: 768px) and (max-width: 1279px){.RijTuc{font-size: 34.0pt;}}@media only screen and (min-width: 1280px){.RijTuc{font-size: 34.0pt;}}@media only screen and (max-width: 479px){.jgG6ef{font-size: 17.0pt;}}@media only screen and (min-width: 480px) and (max-width: 767px){.jgG6ef{font-size: 17.0pt;}}@media only screen and (min-width: 768px) and (max-width: 1279px){.jgG6ef{font-size: 18.0pt;}}@media only screen and (min-width: 1280px){.jgG6ef{font-size: 18.0pt;}}
  </style>
  <link href="https://www.gstatic.com/_/atari/_/ss/k=atari.vw.muEDoYdbUmc.L.W.O/d=1/rs=AGEqA5njKlpjzmlyywIoNpdY65c1cGosIw" nonce="8mzp1G22vLR+L+rvQVdG3w" rel="stylesheet"/>
  <title>
   LunarLander GA
  </title>
  <style jsname="ptDGoc" nonce="8mzp1G22vLR+L+rvQVdG3w">
   .M63kCb{background-color: rgba(255,255,255,1);}.OUGEr{color: rgba(33,33,33,1);}.duRjpb .OUGEr{color: rgba(127,17,70,1);}.JYVBee .OUGEr{color: rgba(127,17,70,1);}.OmQG5e .OUGEr{color: rgba(33,33,33,1);}.iwQgFb{background-color: rgba(0,0,0,0.150000006);}.ySLm4c{font-family: Lato, sans-serif;}.CbiMKe{background-color: rgba(193,40,114,1);}.qeLZfd .zfr3Q{color: rgba(33,33,33,1);}.qeLZfd .qnVSj{color: rgba(33,33,33,1);}.qeLZfd .Glwbz{color: rgba(33,33,33,1);}.qeLZfd .duRjpb{color: rgba(127,17,70,1);}.qeLZfd .qLrapd{color: rgba(127,17,70,1);}.qeLZfd .JYVBee{color: rgba(127,17,70,1);}.qeLZfd .aHM7ed{color: rgba(127,17,70,1);}.qeLZfd .OmQG5e{color: rgba(33,33,33,1);}.qeLZfd .NHD4Gf{color: rgba(33,33,33,1);}.qeLZfd .aw5Odc{color: rgba(161,0,78,1);}.qeLZfd .dhtgD:hover{color: rgba(198,41,109,1);}.qeLZfd .dhtgD:visited{color: rgba(161,0,78,1);}.qeLZfd .iwQgFb{background-color: rgba(0,0,0,0.150000006);}.qeLZfd .OUGEr{color: rgba(33,33,33,1);}.qeLZfd .duRjpb .OUGEr{color: rgba(127,17,70,1);}.qeLZfd .JYVBee .OUGEr{color: rgba(127,17,70,1);}.qeLZfd .OmQG5e .OUGEr{color: rgba(33,33,33,1);}.qeLZfd:before{background-color: rgba(242,242,242,1); display: block;}.lQAHbd .zfr3Q{color: rgba(255,255,255,1);}.lQAHbd .qnVSj{color: rgba(255,255,255,1);}.lQAHbd .Glwbz{color: rgba(255,255,255,1);}.lQAHbd .duRjpb{color: rgba(255,255,255,1);}.lQAHbd .qLrapd{color: rgba(255,255,255,1);}.lQAHbd .JYVBee{color: rgba(255,255,255,1);}.lQAHbd .aHM7ed{color: rgba(255,255,255,1);}.lQAHbd .OmQG5e{color: rgba(255,255,255,1);}.lQAHbd .NHD4Gf{color: rgba(255,255,255,1);}.lQAHbd .aw5Odc{color: rgba(255,255,255,1);}.lQAHbd .dhtgD:hover{color: rgba(255,255,255,1);}.lQAHbd .dhtgD:visited{color: rgba(255,255,255,1);}.lQAHbd .iwQgFb{background-color: rgba(255,255,255,0.150000006);}.lQAHbd .OUGEr{color: rgba(255,255,255,1);}.lQAHbd .duRjpb .OUGEr{color: rgba(255,255,255,1);}.lQAHbd .JYVBee .OUGEr{color: rgba(255,255,255,1);}.lQAHbd .OmQG5e .OUGEr{color: rgba(255,255,255,1);}.lQAHbd .CbiMKe{background-color: rgba(255,255,255,1);}.lQAHbd:before{background-color: rgba(193,40,114,1); display: block;}.cJgDec .zfr3Q{color: rgba(255,255,255,1);}.cJgDec .zfr3Q .OUGEr{color: rgba(255,255,255,1);}.cJgDec .qnVSj{color: rgba(255,255,255,1);}.cJgDec .Glwbz{color: rgba(255,255,255,1);}.cJgDec .qLrapd{color: rgba(255,255,255,1);}.cJgDec .aHM7ed{color: rgba(255,255,255,1);}.cJgDec .NHD4Gf{color: rgba(255,255,255,1);}.cJgDec .IFuOkc:before{background-color: rgba(33,33,33,1); opacity: 0; display: block;}.O13XJf{height: 340px; padding-bottom: 60px; padding-top: 60px;}.O13XJf .IFuOkc{background-color: rgba(127,17,70,1); background-image: url(https://ssl.gstatic.com/atari/images/simple-header-blended-small.png);}.O13XJf .IFuOkc:before{background-color: rgba(33,33,33,1); opacity: 0.4; display: block;}.O13XJf .zfr3Q{color: rgba(255,255,255,1);}.O13XJf .qnVSj{color: rgba(255,255,255,1);}.O13XJf .Glwbz{color: rgba(255,255,255,1);}.O13XJf .duRjpb{color: rgba(255,255,255,1);}.O13XJf .qLrapd{color: rgba(255,255,255,1);}.O13XJf .JYVBee{color: rgba(255,255,255,1);}.O13XJf .aHM7ed{color: rgba(255,255,255,1);}.O13XJf .OmQG5e{color: rgba(255,255,255,1);}.O13XJf .NHD4Gf{color: rgba(255,255,255,1);}.tpmmCb .zfr3Q{color: rgba(33,33,33,1);}.tpmmCb .zfr3Q .OUGEr{color: rgba(33,33,33,1);}.tpmmCb .qnVSj{color: rgba(33,33,33,1);}.tpmmCb .Glwbz{color: rgba(33,33,33,1);}.tpmmCb .qLrapd{color: rgba(33,33,33,1);}.tpmmCb .aHM7ed{color: rgba(33,33,33,1);}.tpmmCb .NHD4Gf{color: rgba(33,33,33,1);}.tpmmCb .IFuOkc:before{background-color: rgba(255,255,255,1); display: block;}.tpmmCb .Wew9ke{fill: rgba(33,33,33,1);}.aw5Odc{color: rgba(161,0,78,1);}.dhtgD:hover{color: rgba(198,41,109,1);}.dhtgD:active{color: rgba(198,41,109,1);}.dhtgD:visited{color: rgba(161,0,78,1);}.Zjiec{color: rgba(255,255,255,1); font-family: Lato, sans-serif; font-size: 19pt; font-weight: 300; letter-spacing: 1px; line-height: 1.3; padding-bottom: 62.5px; padding-left: 48px; padding-right: 36px; padding-top: 11.5px;}.XMyrgf{margin-top: 0px; margin-left: 48px; margin-bottom: 24px; margin-right: 24px;}.TlfmSc{color: rgba(255,255,255,1); font-family: Lato, sans-serif; font-size: 15pt; font-weight: 300; line-height: 1.333;}.Mz8gvb{color: rgba(255,255,255,1);}.zDUgLc{background-color: rgba(33,33,33,1);}.QTKDff.chg4Jd:focus{background-color: rgba(255,255,255,0.1199999973);}.YTv4We{color: rgba(178,178,178,1);}.YTv4We:hover:before{background-color: rgba(255,255,255,0.1199999973); display: block;}.YTv4We.chg4Jd:focus:before{border-color: rgba(255,255,255,0.3600000143); display: block;}.eWDljc{background-color: rgba(33,33,33,1);}.eWDljc .hDrhEe{padding-left: 8px;}.ZXW7w{color: rgba(255,255,255,1); opacity: 0.26;}.PsKE7e{color: rgba(255,255,255,1); font-family: Lato, sans-serif; font-size: 12pt; font-weight: 300;}.lhZOrc{color: rgba(255,77,163,1);}.hDrhEe:hover{color: rgba(255,77,163,1);}.M9vuGd{color: rgba(255,77,163,1); font-weight: 400;}.jgXgSe:hover{color: rgba(255,77,163,1);}.j10yRb:hover{color: rgba(255,77,163,1);}.j10yRb.chg4Jd:focus:before{border-color: rgba(255,255,255,0.3600000143); display: block;}.iWs3gf{color: rgba(255,255,255,1);}.wgxiMe{background-color: rgba(33,33,33,1);}.fOU46b .TlfmSc{color: rgba(255,255,255,1);}.fOU46b .KJll8d{background-color: rgba(255,255,255,1);}.fOU46b .Mz8gvb{color: rgba(255,255,255,1);}.fOU46b .Mz8gvb.chg4Jd:focus:before{border-color: rgba(255,255,255,1); display: block;}.fOU46b .qV4dIc{color: rgba(255,255,255,0.8700000048);}.fOU46b .jgXgSe:hover{color: rgba(255,255,255,1);}.fOU46b .M9vuGd{color: rgba(255,255,255,1);}.fOU46b .iWs3gf{color: rgba(255,255,255,0.8700000048);}.fOU46b .G8QRnc .Mz8gvb{color: rgba(0,0,0,0.8000000119);}.fOU46b .G8QRnc .Mz8gvb.chg4Jd:focus:before{border-color: rgba(0,0,0,0.8000000119); display: block;}.fOU46b .G8QRnc .ZXW7w{color: rgba(0,0,0,0.8000000119);}.fOU46b .G8QRnc .TlfmSc{color: rgba(0,0,0,0.8000000119);}.fOU46b .G8QRnc .KJll8d{background-color: rgba(0,0,0,0.8000000119);}.fOU46b .G8QRnc .qV4dIc{color: rgba(0,0,0,0.6399999857);}.fOU46b .G8QRnc .jgXgSe:hover{color: rgba(0,0,0,0.8199999928);}.fOU46b .G8QRnc .M9vuGd{color: rgba(0,0,0,0.8199999928);}.fOU46b .G8QRnc .iWs3gf{color: rgba(0,0,0,0.6399999857);}.fOU46b .usN8rf .Mz8gvb{color: rgba(0,0,0,0.8000000119);}.fOU46b .usN8rf .Mz8gvb.chg4Jd:focus:before{border-color: rgba(0,0,0,0.8000000119); display: block;}.fOU46b .usN8rf .ZXW7w{color: rgba(0,0,0,0.8000000119);}.fOU46b .usN8rf .TlfmSc{color: rgba(0,0,0,0.8000000119);}.fOU46b .usN8rf .KJll8d{background-color: rgba(0,0,0,0.8000000119);}.fOU46b .usN8rf .qV4dIc{color: rgba(0,0,0,0.6399999857);}.fOU46b .usN8rf .jgXgSe:hover{color: rgba(0,0,0,0.8199999928);}.fOU46b .usN8rf .M9vuGd{color: rgba(0,0,0,0.8199999928);}.fOU46b .usN8rf .iWs3gf{color: rgba(0,0,0,0.6399999857);}.fOU46b .aCIEDd .qV4dIc{color: rgba(33,33,33,1);}.fOU46b .aCIEDd .TlfmSc{color: rgba(33,33,33,1);}.fOU46b .aCIEDd .KJll8d{background-color: rgba(33,33,33,1);}.fOU46b .aCIEDd .ZXW7w{color: rgba(33,33,33,1);}.fOU46b .aCIEDd .jgXgSe:hover{color: rgba(33,33,33,1); opacity: 0.82;}.fOU46b .aCIEDd .Mz8gvb{color: rgba(33,33,33,1);}.fOU46b .aCIEDd .iWs3gf{color: rgba(33,33,33,1);}.fOU46b .a3ETed .qV4dIc{color: rgba(255,255,255,1);}.fOU46b .a3ETed .TlfmSc{color: rgba(255,255,255,1);}.fOU46b .a3ETed .KJll8d{background-color: rgba(255,255,255,1);}.fOU46b .a3ETed .ZXW7w{color: rgba(255,255,255,1);}.fOU46b .a3ETed .jgXgSe:hover{color: rgba(255,255,255,1); opacity: 0.82;}.fOU46b .a3ETed .Mz8gvb{color: rgba(255,255,255,1);}.fOU46b .a3ETed .iWs3gf{color: rgba(255,255,255,1);}@media only screen and (min-width: 1280px){.XeSM4.b2Iqye.fOU46b .LBrwzc .iWs3gf{color: rgba(255,255,255,0.8700000048);}}@media only screen and (min-width: 1280px){.KuNac.b2Iqye.fOU46b .iWs3gf{color: rgba(0,0,0,0.6399999857);}}.fOU46b .zDUgLc{opacity: 0;}.LBrwzc .ZXW7w{color: rgba(0,0,0,1);}.LBrwzc .KJll8d{background-color: rgba(0,0,0,1);}.GBy4H .ZXW7w{color: rgba(255,255,255,1);}.GBy4H .KJll8d{background-color: rgba(255,255,255,1);}.eBSUbc{background-color: rgba(33,33,33,1); color: rgba(0,188,212,0.6999999881);}.BFDQOb:hover{color: rgba(255,77,163,1);}.ImnMyf{background-color: rgba(255,255,255,1); color: rgba(33,33,33,1);}.Vs12Bd{background-color: rgba(242,242,242,1); color: rgba(33,33,33,1);}.S5d9Rd{background-color: rgba(193,40,114,1); color: rgba(255,255,255,1);}.zfr3Q{color: rgba(33,33,33,1); font-family: Lato, sans-serif; font-size: 11pt; font-weight: 400; line-height: 1.6667; margin-top: 12px;}.qnVSj{color: rgba(33,33,33,1);}.Glwbz{color: rgba(33,33,33,1);}.duRjpb{color: rgba(127,17,70,1); font-family: Lato, sans-serif; font-size: 34pt; font-weight: 300; letter-spacing: 0.5px; line-height: 1.2; margin-top: 30px;}.Ap4VC{margin-bottom: -30px;}.qLrapd{color: rgba(127,17,70,1);}.JYVBee{color: rgba(127,17,70,1); font-family: Lato, sans-serif; font-size: 19pt; font-weight: 400; line-height: 1.4; margin-top: 20px;}.CobnVe{margin-bottom: -20px;}.aHM7ed{color: rgba(127,17,70,1);}.OmQG5e{color: rgba(33,33,33,1); font-family: Lato, sans-serif; font-size: 15pt; font-style: normal; font-weight: 400; line-height: 1.25; margin-top: 16px;}.GV3q8e{margin-bottom: -16px;}.NHD4Gf{color: rgba(33,33,33,1);}.LB7kq .duRjpb{font-size: 64pt; letter-spacing: 2px; line-height: 1; margin-top: 40px;}.LB7kq .JYVBee{font-size: 25pt; font-weight: 300; line-height: 1.1; margin-top: 25px;}@media only screen and (max-width: 479px){.LB7kq .duRjpb{font-size: 40pt;}}@media only screen and (min-width: 480px) and (max-width: 767px){.LB7kq .duRjpb{font-size: 53pt;}}@media only screen and (max-width: 479px){.LB7kq .JYVBee{font-size: 19pt;}}@media only screen and (min-width: 480px) and (max-width: 767px){.LB7kq .JYVBee{font-size: 22pt;}}.O13XJf{height: 340px; padding-bottom: 60px; padding-top: 60px;}@media only screen and (min-width: 480px) and (max-width: 767px){.O13XJf{height: 280px; padding-bottom: 40px; padding-top: 40px;}}@media only screen and (max-width: 479px){.O13XJf{height: 250px; padding-bottom: 30px; padding-top: 30px;}}.SBrW1{height: 520px;}@media only screen and (min-width: 480px) and (max-width: 767px){.SBrW1{height: 520px;}}@media only screen and (max-width: 479px){.SBrW1{height: 400px;}}.Wew9ke{fill: rgba(255,255,255,1);}.gk8rDe{height: 180px; padding-bottom: 32px; padding-top: 60px;}.gk8rDe .zfr3Q{color: rgba(0,0,0,1);}.gk8rDe .duRjpb{color: rgba(127,17,70,1); font-size: 45pt; line-height: 1.1;}.gk8rDe .qLrapd{color: rgba(127,17,70,1);}.gk8rDe .JYVBee{color: rgba(127,17,70,1); font-size: 27pt; line-height: 1.35; margin-top: 15px;}.gk8rDe .aHM7ed{color: rgba(127,17,70,1);}.gk8rDe .OmQG5e{color: rgba(33,33,33,1);}.gk8rDe .NHD4Gf{color: rgba(33,33,33,1);}@media only screen and (max-width: 479px){.gk8rDe .duRjpb{font-size: 30pt;}}@media only screen and (min-width: 480px) and (max-width: 767px){.gk8rDe .duRjpb{font-size: 38pt;}}@media only screen and (max-width: 479px){.gk8rDe .JYVBee{font-size: 20pt;}}@media only screen and (min-width: 480px) and (max-width: 767px){.gk8rDe .JYVBee{font-size: 24pt;}}@media only screen and (min-width: 480px) and (max-width: 767px){.gk8rDe{padding-top: 45px;}}@media only screen and (max-width: 479px){.gk8rDe{padding-bottom: 0px; padding-top: 30px;}}.dhtgD{text-decoration: underline;}.JzO0Vc{background-color: rgba(33,33,33,1); font-family: Lato, sans-serif; width: 250px;}@media only screen and (min-width: 1280px){.JzO0Vc{padding-top: 48.5px;}}.TlfmSc{font-family: Lato, sans-serif; font-size: 15pt; font-weight: 300; line-height: 1.333;}.PsKE7e{font-family: Lato, sans-serif; font-size: 12pt;}.IKA38e{line-height: 1.21;}.hDrhEe{padding-bottom: 11.5px; padding-top: 11.5px;}.zDUgLc{opacity: 1;}.QmpIrf{background-color: rgba(193,40,114,1); border-color: rgba(255,255,255,1); color: rgba(255,255,255,1); font-family: Lato, sans-serif; font-size: 11pt; line-height: normal;}.xkUom{border-color: rgba(193,40,114,1); color: rgba(193,40,114,1); font-family: Lato, sans-serif; font-size: 11pt; line-height: normal;}.xkUom:hover{background-color: rgba(193,40,114,0.1000000015);}.KjwKmc{color: rgba(193,40,114,1); font-family: Lato, sans-serif; font-size: 11pt; line-height: normal; line-height: normal;}.KjwKmc:hover{background-color: rgba(193,40,114,0.1000000015);}.lQAHbd .QmpIrf{background-color: rgba(255,255,255,1); border-color: rgba(127,17,70,1); color: rgba(127,17,70,1); font-family: Lato, sans-serif; font-size: 11pt; line-height: normal;}.lQAHbd .xkUom{border-color: rgba(242,242,242,1); color: rgba(242,242,242,1); font-family: Lato, sans-serif; font-size: 11pt; line-height: normal;}.lQAHbd .xkUom:hover{background-color: rgba(255,255,255,0.1000000015);}.lQAHbd .KjwKmc{color: rgba(242,242,242,1); font-family: Lato, sans-serif; font-size: 11pt; line-height: normal;}.lQAHbd .KjwKmc:hover{background-color: rgba(255,255,255,0.1000000015);}.cJgDec .QmpIrf{background-color: rgba(255,255,255,1); border-color: rgba(127,17,70,1); color: rgba(127,17,70,1); font-family: Lato, sans-serif; font-size: 11pt; line-height: normal;}.cJgDec .xkUom{border-color: rgba(242,242,242,1); color: rgba(242,242,242,1); font-family: Lato, sans-serif; font-size: 11pt; line-height: normal;}.cJgDec .xkUom:hover{background-color: rgba(255,255,255,0.1000000015);}.cJgDec .KjwKmc{color: rgba(242,242,242,1); font-family: Lato, sans-serif; font-size: 11pt; line-height: normal;}.cJgDec .KjwKmc:hover{background-color: rgba(255,255,255,0.1000000015);}.tpmmCb .QmpIrf{background-color: rgba(255,255,255,1); border-color: rgba(127,17,70,1); color: rgba(127,17,70,1); font-family: Lato, sans-serif; font-size: 11pt; line-height: normal;}.tpmmCb .xkUom{border-color: rgba(193,40,114,1); color: rgba(193,40,114,1); font-family: Lato, sans-serif; font-size: 11pt; line-height: normal;}.tpmmCb .xkUom:hover{background-color: rgba(193,40,114,0.1000000015);}.tpmmCb .KjwKmc{color: rgba(193,40,114,1); font-family: Lato, sans-serif; font-size: 11pt; line-height: normal;}.tpmmCb .KjwKmc:hover{background-color: rgba(193,40,114,0.1000000015);}.gk8rDe .QmpIrf{background-color: rgba(193,40,114,1); border-color: rgba(255,255,255,1); color: rgba(255,255,255,1); font-family: Lato, sans-serif; font-size: 11pt; line-height: normal;}.gk8rDe .xkUom{border-color: rgba(193,40,114,1); color: rgba(193,40,114,1); font-family: Lato, sans-serif; font-size: 11pt; line-height: normal;}.gk8rDe .xkUom:hover{background-color: rgba(193,40,114,0.1000000015);}.gk8rDe .KjwKmc{color: rgba(193,40,114,1); font-family: Lato, sans-serif; font-size: 11pt; line-height: normal;}.gk8rDe .KjwKmc:hover{background-color: rgba(193,40,114,0.1000000015);}.O13XJf .QmpIrf{background-color: rgba(255,255,255,1); border-color: rgba(127,17,70,1); color: rgba(127,17,70,1); font-family: Lato, sans-serif; font-size: 11pt; line-height: normal;}.O13XJf .xkUom{border-color: rgba(242,242,242,1); color: rgba(242,242,242,1); font-family: Lato, sans-serif; font-size: 11pt; line-height: normal;}.O13XJf .xkUom:hover{background-color: rgba(255,255,255,0.1000000015);}.O13XJf .KjwKmc{color: rgba(242,242,242,1); font-family: Lato, sans-serif; font-size: 11pt; line-height: normal;}.O13XJf .KjwKmc:hover{background-color: rgba(255,255,255,0.1000000015);}.Y4CpGd{font-family: Lato, sans-serif; font-size: 11pt;}.CMArNe{background-color: rgba(242,242,242,1);}.LBrwzc .TlfmSc{color: rgba(0,0,0,0.8000000119);}.LBrwzc .YTv4We{color: rgba(0,0,0,0.6399999857);}.LBrwzc .YTv4We.chg4Jd:focus:before{border-color: rgba(0,0,0,0.6399999857); display: block;}.LBrwzc .Mz8gvb{color: rgba(0,0,0,0.6399999857);}.LBrwzc .iWs3gf{color: rgba(0,0,0,0.6399999857);}.LBrwzc .wgxiMe{background-color: rgba(255,255,255,1);}.LBrwzc .qV4dIc{color: rgba(0,0,0,0.6399999857);}.LBrwzc .M9vuGd{color: rgba(0,0,0,0.8000000119); font-weight: bold;}.LBrwzc .Zjiec{color: rgba(0,0,0,0.8000000119);}.LBrwzc .IKA38e{color: rgba(0,0,0,0.6399999857);}.LBrwzc .lhZOrc.IKA38e{color: rgba(0,0,0,0.8000000119); font-weight: bold;}.LBrwzc .j10yRb:hover{color: rgba(0,0,0,0.8000000119);}.LBrwzc .eBSUbc{color: rgba(0,0,0,0.8000000119);}.LBrwzc .hDrhEe:hover{color: rgba(0,0,0,0.8000000119);}.LBrwzc .jgXgSe:hover{color: rgba(0,0,0,0.8000000119);}.LBrwzc .M9vuGd:hover{color: rgba(0,0,0,0.8000000119);}.LBrwzc .zDUgLc{border-bottom-color: rgba(204,204,204,1); border-bottom-width: 1px; border-bottom-style: solid;}.fOU46b .LBrwzc .M9vuGd{color: rgba(0,0,0,0.8000000119);}.fOU46b .LBrwzc .jgXgSe:hover{color: rgba(0,0,0,0.8000000119);}.fOU46b .LBrwzc .zDUgLc{opacity: 1; border-bottom-style: none;}.fOU46b .LBrwzc .iWs3gf{color: rgba(0,0,0,0.6399999857);}.fOU46b .GBy4H .M9vuGd{color: rgba(255,255,255,1);}.fOU46b .GBy4H .jgXgSe:hover{color: rgba(255,255,255,1);}.fOU46b .GBy4H .zDUgLc{opacity: 1;}.fOU46b .GBy4H .iWs3gf{color: rgba(255,255,255,0.8700000048);}.XeSM4.G9Qloe.fOU46b .LBrwzc .iWs3gf{color: rgba(0,0,0,0.6399999857);}.GBy4H .lhZOrc.IKA38e{color: rgba(255,255,255,1);}.GBy4H .eBSUbc{color: rgba(255,255,255,0.8700000048);}.GBy4H .hDrhEe:hover{color: rgba(255,255,255,1);}.GBy4H .j10yRb:hover{color: rgba(255,255,255,1);}.GBy4H .YTv4We{color: rgba(255,255,255,1);}.GBy4H .YTv4We.chg4Jd:focus:before{border-color: rgba(255,255,255,1); display: block;}.GBy4H .iWs3gf{color: rgba(255,255,255,0.8700000048);}.GBy4H .jgXgSe:hover{color: rgba(255,255,255,1);}.GBy4H .jgXgSe:hover{color: rgba(255,255,255,1);}.GBy4H .M9vuGd{color: rgba(255,255,255,1);}.GBy4H .M9vuGd:hover{color: rgba(255,255,255,1);}.QcmuFb{padding-left: 20px;}.vDPrib{padding-left: 40px;}.TBDXjd{padding-left: 60px;}.bYeK8e{padding-left: 80px;}.CuqSDe{padding-left: 100px;}.Havqpe{padding-left: 120px;}.JvDrRe{padding-left: 140px;}.o5lrIf{padding-left: 160px;}.yOJW7c{padding-left: 180px;}.rB8cye{padding-left: 200px;}.RuayVd{padding-right: 20px;}.YzcKX{padding-right: 40px;}.reTV0b{padding-right: 60px;}.vSYeUc{padding-right: 80px;}.PxtZIe{padding-right: 100px;}.ahQMed{padding-right: 120px;}.rzhcXb{padding-right: 140px;}.PBhj0b{padding-right: 160px;}.TlN46c{padding-right: 180px;}.GEdNnc{padding-right: 200px;}.TMjjoe{font-family: Lato, sans-serif; font-size: 9pt; line-height: 1.2; margin-top: 0px;}@media only screen and (min-width: 1280px){.yxgWrb{margin-left: 250px;}}@media only screen and (max-width: 479px){.Zjiec{font-size: 15pt;}}@media only screen and (min-width: 480px) and (max-width: 767px){.Zjiec{font-size: 17pt;}}@media only screen and (max-width: 479px){.TlfmSc{font-size: 13pt;}}@media only screen and (min-width: 480px) and (max-width: 767px){.TlfmSc{font-size: 14pt;}}@media only screen and (max-width: 479px){.PsKE7e{font-size: 12pt;}}@media only screen and (min-width: 480px) and (max-width: 767px){.PsKE7e{font-size: 12pt;}}@media only screen and (max-width: 479px){.duRjpb{font-size: 24pt;}}@media only screen and (min-width: 480px) and (max-width: 767px){.duRjpb{font-size: 29pt;}}@media only screen and (max-width: 479px){.JYVBee{font-size: 15pt;}}@media only screen and (min-width: 480px) and (max-width: 767px){.JYVBee{font-size: 17pt;}}@media only screen and (max-width: 479px){.OmQG5e{font-size: 13pt;}}@media only screen and (min-width: 480px) and (max-width: 767px){.OmQG5e{font-size: 14pt;}}@media only screen and (max-width: 479px){.TlfmSc{font-size: 13pt;}}@media only screen and (min-width: 480px) and (max-width: 767px){.TlfmSc{font-size: 14pt;}}@media only screen and (max-width: 479px){.PsKE7e{font-size: 12pt;}}@media only screen and (min-width: 480px) and (max-width: 767px){.PsKE7e{font-size: 12pt;}}@media only screen and (max-width: 479px){.TMjjoe{font-size: 9pt;}}@media only screen and (min-width: 480px) and (max-width: 767px){.TMjjoe{font-size: 9pt;}}section[id="h.4a9d518ede350020_0"] .IFuOkc:before{opacity: 0.0;}section[id="h.3362346e3d12c940_136"] .IFuOkc:before{opacity: 0.6;}
  </style>
  <script nonce="PlDSnyC9Wpbidv1t4uPZIw">
   _at_config = [null,"AIzaSyChg3MFqzdi1P5J-YvEyakkSA1yU7HRcDI","897606708560-a63d8ia0t9dhtpdt4i3djab2m42see7o.apps.googleusercontent.com",null,null,"v2",null,null,null,null,null,null,null,"https://content.googleapis.com","SITES_%s",null,null,null,null,null,null,null,null,null,["AHKXmL2l1dbdY7115XsqthttbdYLXv8snocwVzJAE5bIRtmLXEmSdreQnphN0vbTiLuDv3NQ1hn0",1,"CJPi0bKqhPQCFQ6FIwAdxVsK5Q",1636222121570000,[5703839,5704621,5706832,5706836,5707711,5708870,5711808,5713049,5713207,5714550,5714628,5720060,5720925,5729664,5732942,5734571,5734954,5735806,5736243,5737337,5738509,5738529,5739802,5739897,5740814,5740908,5741775,5742462,5743124,5745622,5745792,5747261,5747741,5748029,5749140,5752694,5753329,5754229,14101306,14101502,14101510,14101530,14101534]],null,null,null,null,0,null,null,null,null,null,null,null,null,null,"https://drive.google.com",null,null,null,null,null,null,1,1,null,0,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"v2internal","https://docs.google.com",null,null,null,null,null,null,"https://sites.google.com/new/",null,null,null,null,null,0,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,"",null,null,null,null,null,null,null,null,null,null,null,null,6,null,null,"https://accounts.google.com/o/oauth2/auth","https://accounts.google.com/o/oauth2/postmessageRelay",null,null,null,null,78,"https://sites.google.com/new/?usp\u003dviewer_footer",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"https://www.gstatic.com/atari/embeds/7925c5f8e01bacb9b4b0a3783ae0b867/intermediate-frame-minified.html",0,null,"v2beta",null,null,null,null,null,null,4,"https://accounts.google.com/o/oauth2/iframe",null,null,null,null,null,null,"https://1801957484-atari-embeds.googleusercontent.com/embeds/16cb204cf3a9d4d223a0a3fd8b0eec5d/inner-frame-minified.html",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,"https://sites.google.com/gapp.nthu.edu.tw/lunarlander-ga",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0,null,null,null,null,null,null,0,null,"",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0,null,null,null,null,null,null,null,null,null,null,null,null,null,0,null,1,null,null,[1636222121580,"atari_2021.43-Tue-0500_RC03","406838597",null,1,1],null,null,null,null,0,null,null,0,null,0,0,null,null,null,null,0,20,500,"https://domains.google.com",null,0,null,null,null,null,null,0,null,null,0,null,null,0,0,1,0,0,0]; window.globals = {"enableAnalytics":true,"webPropertyId":"","showDebug":false,"hashedSiteId":"efbce97cbe827e9534b7db698abb0e675bf9e3246033b4006a7f2d9e016c2f4a","normalizedPath":"gapp.nthu.edu.tw/lunarlander-ga/lunarlander","pageTitle":"LunarLander"}; function gapiLoaded() {if (globals.gapiLoaded == undefined) {globals.gapiLoaded = true;} else {globals.gapiLoaded();}}window.messages = []; window.addEventListener && window.addEventListener('message', function(e) {if (window.messages && e.data && e.data.magic == 'SHIC') {window.messages.push(e);}});
  </script>
  <script nonce="PlDSnyC9Wpbidv1t4uPZIw" src="https://apis.google.com/js/client.js?onload=gapiLoaded">
  </script>
  <script nonce="PlDSnyC9Wpbidv1t4uPZIw">
   (function(){/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
/*

 Copyright 2011 Google LLC.
 SPDX-License-Identifier: Apache-2.0
*/
/*

 Copyright 2013 Google LLC.
 SPDX-License-Identifier: Apache-2.0
*/
/*

 Copyright 2020 Google LLC.
 SPDX-License-Identifier: Apache-2.0
*/
var a=(this||self)._jsa||{};a._cfc=void 0;a._aeh=void 0;/*

 Copyright 2005 Google LLC.
 SPDX-License-Identifier: Apache-2.0
*/
}).call(this);
  </script>
  <script nonce="PlDSnyC9Wpbidv1t4uPZIw">
   const imageUrl = 'https:\/\/lh4.googleusercontent.com\/bugwS8GY-rzazZcWghCzJp-XChmE7UERFHMrFBJu8SYpC7JYZkVIt465q49gD_dqxwW-FoYN3JmOxscmC3FmM3A\x3dw16383';
      function bgImgLoaded() {
        if (!globals.headerBgImgLoaded) {
          globals.headerBgImgLoaded = new Date().getTime();
        } else {
          globals.headerBgImgLoaded();
        }
      }
      if (imageUrl) {
        const img = new Image();
        img.src = imageUrl;
        img.onload = bgImgLoaded;
        globals.headerBgImgExists = true;
      } else {
        globals.headerBgImgExists = false;
      }
  </script>
 </head>
 <body css="yDmH0d" dir="ltr" id="yDmH0d" itemscope="" itemtype="http://schema.org/WebPage">
  <div jsaction="rcuQ6b:WYd;GvneHb:og1FDd;vbaUQc:uAM5ec;YBArc:dj7Cne;" jscontroller="pc62j" jsmodel="iTeaXe">
   <div jsaction="rcuQ6b:WYd;o6xM5b:Pg9eo;HuL2Hd:mHeCvf;VMhF5:FFYy5e;sk3Qmb:HI1Mdd;" jscontroller="X4BaPc">
    <div data-domain="gapp.nthu.edu.tw" data-sitename="lunarlander-ga" data-universe="1" jsaction="Pe9H6d:cZFEp;WMZaJ:VsGN3;hJluRd:UADL7b;zuqEgd:HI9w0;tr6QDd:Y8aXB;MxH79b:xDkBfb;JIbuQc:SPXMTb(uxAMZ);" jscontroller="o1L5Wb" jsmodel="fNFZH" jsname="G0jgYd">
     <div class="p9b27" jsname="gYwusb">
     </div>
     <div jsaction="keydown:uiKYid(OH0EC);rcuQ6b:WYd;zuqEgd:ufqpf;JIbuQc:XfTnxb(lfEfFf),AlTiYc(GeGHKb),AlTiYc(m1xNUe),zZlNMe(pZn8Oc);YqO5N:ELcyfe;" jscontroller="RrXLpc" jsname="XeeWQc" role="banner">
      <div class="BuY5Fd" jsaction="click:xVuwSc;" jsname="bF1uUb">
      </div>
      <div class="TbNlJb" jsname="MVsrn">
       <div aria-disabled="false" aria-label="Back to site" class="U26fgb mUbCce fKz7Od h3nfre M9Bg4d" data-tooltip="Back to site" data-tooltip-horizontal-offset="0" data-tooltip-vertical-offset="-12" jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue; focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef;touchstart:p6p2H; touchmove:FwuNnf; touchend:yfqBxc(preventMouseEvents=true|preventDefault=true); touchcancel:JMtRjd;" jscontroller="VXdfxd" jsname="GeGHKb" jsshadow="" role="button" tabindex="0">
        <div class="VTBa7b MbhUzd" jsname="ksKsZd">
        </div>
        <span class="xjKiLb" jsslot="">
         <span class="Ce1Y1c" style="top: -12px">
          <svg class="V4YR2c" focusable="false" viewbox="0 0 24 24">
           <path d="M0 0h24v24H0z" fill="none">
           </path>
           <path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z">
           </path>
          </svg>
         </span>
        </span>
       </div>
       <div class="E2UJ5" jsname="M6JdT">
        <div aria-expanded="true" class="rFrNMe b7AJhc zKHdkd" jsaction="clickonly:KjsqPd; focus:Jt1EX; blur:fpfTEe; input:Lg5SV" jscontroller="pxq3x" jsname="OH0EC" jsshadow="">
         <div class="aCsJod oJeWuf">
          <div class="aXBtI I0VJ4d Wic03c">
           <span class="A37UZe qgcB3c iHd5yb" jsslot="">
            <div aria-disabled="false" aria-label="Search" class="U26fgb mUbCce fKz7Od i3PoXe M9Bg4d" data-tooltip="Search" data-tooltip-horizontal-offset="0" data-tooltip-vertical-offset="-12" jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue; focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef;touchstart:p6p2H; touchmove:FwuNnf; touchend:yfqBxc(preventMouseEvents=true|preventDefault=true); touchcancel:JMtRjd;" jscontroller="VXdfxd" jsname="lfEfFf" jsshadow="" role="button" tabindex="0">
             <div class="VTBa7b MbhUzd" jsname="ksKsZd">
             </div>
             <span class="xjKiLb" jsslot="">
              <span class="Ce1Y1c" style="top: -12px">
               <svg class="vu8Pwe" focusable="false" viewbox="0 0 24 24">
                <path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z">
                </path>
                <path d="M0 0h24v24H0z" fill="none">
                </path>
               </svg>
              </span>
             </span>
            </div>
            <div class="EmVfjc SKShhf" data-loadingmessage="Loading…" jsaction="animationend:kWijWc;dyRcpb:dyRcpb" jscontroller="qAKInc" jsname="aZ2wEe">
             <div aria-live="assertive" class="Cg7hO" jsname="vyyg5">
             </div>
             <div class="xu46lf" jsname="Hxlbvc">
              <div class="ir3uv uWlRce co39ub">
               <div class="xq3j6 ERcjC">
                <div class="X6jHbb GOJTSe">
                </div>
               </div>
               <div class="HBnAAc">
                <div class="X6jHbb GOJTSe">
                </div>
               </div>
               <div class="xq3j6 dj3yTd">
                <div class="X6jHbb GOJTSe">
                </div>
               </div>
              </div>
              <div class="ir3uv GFoASc Cn087">
               <div class="xq3j6 ERcjC">
                <div class="X6jHbb GOJTSe">
                </div>
               </div>
               <div class="HBnAAc">
                <div class="X6jHbb GOJTSe">
                </div>
               </div>
               <div class="xq3j6 dj3yTd">
                <div class="X6jHbb GOJTSe">
                </div>
               </div>
              </div>
              <div class="ir3uv WpeOqd hfsr6b">
               <div class="xq3j6 ERcjC">
                <div class="X6jHbb GOJTSe">
                </div>
               </div>
               <div class="HBnAAc">
                <div class="X6jHbb GOJTSe">
                </div>
               </div>
               <div class="xq3j6 dj3yTd">
                <div class="X6jHbb GOJTSe">
                </div>
               </div>
              </div>
              <div class="ir3uv rHV3jf EjXFBf">
               <div class="xq3j6 ERcjC">
                <div class="X6jHbb GOJTSe">
                </div>
               </div>
               <div class="HBnAAc">
                <div class="X6jHbb GOJTSe">
                </div>
               </div>
               <div class="xq3j6 dj3yTd">
                <div class="X6jHbb GOJTSe">
                </div>
               </div>
              </div>
             </div>
            </div>
            <div aria-disabled="false" aria-label="Back to site" class="U26fgb mUbCce fKz7Od JyJRXe M9Bg4d" data-tooltip="Back to site" data-tooltip-horizontal-offset="0" data-tooltip-vertical-offset="-12" jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue; focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef;touchstart:p6p2H; touchmove:FwuNnf; touchend:yfqBxc(preventMouseEvents=true|preventDefault=true); touchcancel:JMtRjd;" jscontroller="VXdfxd" jsname="m1xNUe" jsshadow="" role="button" tabindex="0">
             <div class="VTBa7b MbhUzd" jsname="ksKsZd">
             </div>
             <span class="xjKiLb" jsslot="">
              <span class="Ce1Y1c" style="top: -12px">
               <svg class="V4YR2c" focusable="false" viewbox="0 0 24 24">
                <path d="M0 0h24v24H0z" fill="none">
                </path>
                <path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z">
                </path>
               </svg>
              </span>
             </span>
            </div>
           </span>
           <div class="Xb9hP">
            <input aria-label="Search this site" autocomplete="off" autofocus="" class="whsOnd zHQkBf" data-initial-value="" jsname="YPqjbf" role="combobox" tabindex="0" type="search" value=""/>
            <div aria-hidden="true" class="ndJi5d snByac" jsname="LwH6nd">
             Search this site
            </div>
           </div>
           <span class="A37UZe sxyYjd MQL3Ob" jsslot="">
            <div aria-disabled="false" aria-label="Clear search" class="U26fgb mUbCce fKz7Od Kk06A M9Bg4d" data-tooltip="Clear search" data-tooltip-horizontal-offset="0" data-tooltip-vertical-offset="-12" jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue; focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef;touchstart:p6p2H; touchmove:FwuNnf; touchend:yfqBxc(preventMouseEvents=true|preventDefault=true); touchcancel:JMtRjd;" jscontroller="VXdfxd" jsname="pZn8Oc" jsshadow="" role="button" tabindex="0">
             <div class="VTBa7b MbhUzd" jsname="ksKsZd">
             </div>
             <span class="xjKiLb" jsslot="">
              <span class="Ce1Y1c" style="top: -12px">
               <svg class="fAUEUd" focusable="false" viewbox="0 0 24 24">
                <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z">
                </path>
                <path d="M0 0h24v24H0z" fill="none">
                </path>
               </svg>
              </span>
             </span>
            </div>
           </span>
           <div class="i9lrp mIZh1c">
           </div>
           <div class="OabDMe cXrdqd" jsname="XmnwAc">
           </div>
          </div>
         </div>
         <div class="LXRPh">
          <div class="ovnfwe Is7Fhb" jsname="ty6ygf">
          </div>
         </div>
        </div>
       </div>
      </div>
     </div>
    </div>
    <div jsname="tiN4bf">
     <div class="M63kCb">
     </div>
     <div class="fktJzd AKpWA fOU46b yMcSQd Ly6Unf G9Qloe XeSM4" data-uses-custom-theme="false" jsaction="gsiSmd:Ffcznf;yj5fUd:cpPetb;HNXL3:q0Vyke;rcuQ6b:WYd;" jscontroller="Md9ENb" jsname="UzWXSb">
      <header id="atIdViewHeader">
       <div class="BbxBP HP6J1d" data-is-preview="false" data-top-navigation="false" jsaction="rcuQ6b:ywL4Jf;VbOlFf:ywL4Jf;FaOgy:ywL4Jf; keydown:Hq2uPe; wheel:Ut4Ahc;" jscontroller="RQOkef" jsname="WA9qLc">
        <div class="VLoccc ELAV1d" jsname="rtFGi">
         <div class="Pvc6xe">
          <div class="TlfmSc YSH9J" jsname="I8J07e">
           <a class="GAuSPc" href="/gapp.nthu.edu.tw/lunarlander-ga/lunarlander" jsname="jIujaf">
            <span class="QTKDff">
             LunarLander GA
            </span>
           </a>
          </div>
         </div>
         <div class="zDUgLc" jsname="mADGA">
         </div>
        </div>
       </div>
       <script nonce="PlDSnyC9Wpbidv1t4uPZIw">
        DOCS_timing['navv'] = new Date().getTime();
       </script>
      </header>
      <div class="UtePc RCETm" dir="ltr" role="main">
       <section class="yaqOZd LB7kq cJgDec nyKByd O13XJf" id="h.4a9d518ede350020_0" style="">
        <div class="Nu95r">
         <div class="IFuOkc" jsname="LQX2Vd" style="background-size: cover; background-position: center center; background-image: url(https://lh4.googleusercontent.com/bugwS8GY-rzazZcWghCzJp-XChmE7UERFHMrFBJu8SYpC7JYZkVIt465q49gD_dqxwW-FoYN3JmOxscmC3FmM3A=w16383);">
         </div>
        </div>
        <div class="mYVXT">
         <div class="LS81yb VICjCf" tabindex="-1">
          <div class="hJDwNd-AhqUyc-uQSCkd purZT-AhqUyc-II5mzb pSzOP-AhqUyc-qWD73c JNdkSc yYI8W">
           <div class="JNdkSc-SmKAyb">
            <div class="" jsaction="zXBUYb:zTPCnb;zQF9Uc:Qxe3nd;" jscontroller="sGwD4d" jsname="F57UId">
             <div class="oKdM2c Kzv0Me">
              <div class="hJDwNd-AhqUyc-uQSCkd jXK9ad D2fZ2 OjCsFc GNzUNc" id="h.3362346e3d12c940_0">
               <div class="jXK9ad-SmKAyb">
                <div class="tyJCtd mGzaTb baZpAe">
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="text-align: center;">
                  <span class="OGiC0d" style="font-family: 'Lato'; font-variant: normal; font-weight: normal; vertical-align: baseline;">
                   Introduction to AI @ NTHU PME
                  </span>
                 </p>
                </div>
               </div>
              </div>
             </div>
             <div class="oKdM2c">
              <div class="hJDwNd-AhqUyc-uQSCkd jXK9ad D2fZ2 wHaque GNzUNc" id="h.12eabc9bace210f0_18">
               <div class="jXK9ad-SmKAyb">
                <div class="tyJCtd mGzaTb baZpAe">
                 <h2 class="CDt4Ke zfr3Q JYVBee" dir="ltr" id="h.ahdiep27b6go" style="text-align: center;">
                  <span class="puwcIf" style="font-family: 'Lato'; font-weight: normal; vertical-align: baseline;">
                   A
                  </span>
                  <span class="puwcIf" style="font-family: 'Lato'; font-variant: normal; font-weight: normal; vertical-align: baseline;">
                   GA-driven Lunar
                  </span>
                  <span class="puwcIf" style="font-family: 'Lato'; font-weight: normal; vertical-align: baseline;">
                   Lander
                  </span>
                 </h2>
                 <p class="CDt4Ke zfr3Q" dir="ltr">
                  <br/>
                 </p>
                 <p class="CDt4Ke zfr3Q" dir="ltr">
                  <br/>
                 </p>
                 <p class="CDt4Ke zfr3Q" dir="ltr">
                  <br/>
                 </p>
                </div>
               </div>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
        </div>
       </section>
       <section class="yaqOZd" id="h.12eabc9bace210f0_51" style="">
        <div class="IFuOkc">
        </div>
        <div class="mYVXT">
         <div class="LS81yb VICjCf" tabindex="-1">
          <div class="hJDwNd-AhqUyc-wNfPc purZT-AhqUyc-II5mzb pSzOP-AhqUyc-wNfPc JNdkSc yYI8W">
           <div class="JNdkSc-SmKAyb">
            <div class="" jsaction="zXBUYb:zTPCnb;zQF9Uc:Qxe3nd;" jscontroller="sGwD4d" jsname="F57UId">
             <div class="oKdM2c Kzv0Me">
              <div class="hJDwNd-AhqUyc-wNfPc pSzOP-AhqUyc-wNfPc jXK9ad D2fZ2 OjCsFc" id="h.12eabc9bace210f0_60">
               <div class="jXK9ad-SmKAyb">
                <div class="tyJCtd baZpAe">
                 <div class="t3iYD">
                  <img class="CENy8b" role="img" src="https://lh4.googleusercontent.com/PfrVybI-4e1TV7XWqNIddQobs1duxwU1F5yDsrll8KVUE0g2XF8rD2Ge6cLRzMmqyRdK_M_mAYrRGijz0Htm0CIu4w4V6dXoIPtngoCAYLmkggpv1kdKgKcfT3m-IcIlPQ=w1280"/>
                 </div>
                </div>
               </div>
              </div>
             </div>
             <div class="oKdM2c">
              <div class="hJDwNd-AhqUyc-wNfPc pSzOP-AhqUyc-wNfPc jXK9ad D2fZ2 wHaque GNzUNc" id="h.344a5156fa92aa0d_5">
               <div class="jXK9ad-SmKAyb">
                <div class="tyJCtd mGzaTb baZpAe">
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="text-align: center;">
                  Image credit:
                  <span class="aw5Odc" style="font-family: 'Arial'; font-weight: normal; text-decoration: underline;">
                   <a class="XqQF9c" href="https://www.google.com/url?q=https%3A%2F%2Fgym.openai.com%2Fenvs%2FLunarLanderContinuous-v2%2F&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNE7YNQW8m48NdtIL8b3ROkb_kYVfA" target="_blank">
                    Gym (openai.com)
                   </a>
                  </span>
                  <span style="color: #000000; font-family: 'Arial'; font-weight: normal;">
                  </span>
                 </p>
                </div>
               </div>
              </div>
             </div>
            </div>
           </div>
          </div>
          <div class="hJDwNd-AhqUyc-OwsYgb purZT-AhqUyc-II5mzb pSzOP-AhqUyc-qWD73c JNdkSc yYI8W">
           <div class="JNdkSc-SmKAyb">
            <div class="" jsaction="zXBUYb:zTPCnb;zQF9Uc:Qxe3nd;" jscontroller="sGwD4d" jsname="F57UId">
             <div class="oKdM2c Kzv0Me">
              <div class="hJDwNd-AhqUyc-OwsYgb jXK9ad D2fZ2 OjCsFc GNzUNc" id="h.12eabc9bace210f0_57">
               <div class="jXK9ad-SmKAyb">
                <div class="tyJCtd mGzaTb baZpAe">
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.38;">
                  <span class="RijTuc" style="color: #226e93; font-family: 'Lato'; font-variant: normal; font-weight: 300; vertical-align: baseline;">
                   You will learn to solve problem using genetic algorithm (GA)
                  </span>
                  <span class="RijTuc" style="color: #226e93; font-family: 'Lato'; font-weight: 300; vertical-align: baseline;">
                   .
                  </span>
                 </p>
                </div>
               </div>
              </div>
             </div>
             <div class="oKdM2c">
              <div class="hJDwNd-AhqUyc-OwsYgb jXK9ad D2fZ2 wHaque GNzUNc" id="h.12eabc9bace210f0_59">
               <div class="jXK9ad-SmKAyb">
                <div class="tyJCtd mGzaTb baZpAe">
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="text-align: justify; white-space: normal;">
                  <span style="color: #212121;">
                   LunarLander is a game in Open AI Gym. In this game, the task is to navigate the lander to the landing pad. By precisely controlling the lander's main engine and side engines, which produce the vertical and horizontal thrust, the lander can land on pad safely.
                  </span>
                 </p>
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="text-align: justify; white-space: normal;">
                  <span style="color: #212121;">
                   A safety landing on the landing pad gets a positive reward. A safety landing outside the landing pad gets no reward. Crashing the lander
                  </span>
                  <span style="color: #212121; font-variant: normal;">
                   yields
                  </span>
                  <span style="color: #212121;">
                   a huge negative reward. In addition, the total fuel consumption is converted into a negative reward. In other words, your lander is expected to perform a safe, precise, and fuel-efficient maneuver to maximize the reward received.
                  </span>
                 </p>
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="text-align: left;">
                  <br/>
                 </p>
                </div>
               </div>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
        </div>
       </section>
       <section class="yaqOZd" id="h.12eabc9bace210f0_235" style="">
        <div class="IFuOkc">
        </div>
        <div class="mYVXT">
         <div class="LS81yb VICjCf" tabindex="-1">
          <div class="hJDwNd-AhqUyc-uQSCkd purZT-AhqUyc-II5mzb pSzOP-AhqUyc-qWD73c JNdkSc">
           <div class="JNdkSc-SmKAyb">
            <div class="" jsaction="zXBUYb:zTPCnb;zQF9Uc:Qxe3nd;" jscontroller="sGwD4d" jsname="F57UId">
             <div class="oKdM2c Kzv0Me">
              <div class="hJDwNd-AhqUyc-uQSCkd jXK9ad D2fZ2 OjCsFc wHaque GNzUNc" id="h.12eabc9bace210f0_238">
               <div class="jXK9ad-SmKAyb">
                <div class="tyJCtd mGzaTb baZpAe">
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.38;">
                  <span class="jgG6ef" style="color: #226e93; vertical-align: baseline;">
                   Problem Description
                  </span>
                 </p>
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="margin-left: 0; padding-left: 0; text-align: justify; text-indent: 0; white-space: normal;">
                  In this assignment, you are asked to optimize the control policy of the lunar lander with genetic algorithm (GA). The lunar lander continuously observes its status and the environment and pilots itself according to the control policy you provided. We have implemented a GA and testing framework for you. Your task is to design and implement the evolutionary operators and tune the parameters for GA so that GA works effectively and efficiently.
                 </p>
                 <ul class="n8H08c UVNKR" style="list-style-type: square; margin-left: 0; margin-right: 0; padding: 0;">
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.2; margin-left: 0; padding-left: 0; text-indent: 0;">
                    <span style="font-family: 'Lato';">
                     <strong>
                      Observation
                     </strong>
                    </span>
                   </p>
                  </li>
                 </ul>
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.2; margin-left: 15pt; padding-left: 0; text-indent: 0;">
                  For every time stamp, the lunar lander receives an observation vector which contains the following dimensions:
                 </p>
                 <ul class="n8H08c UVNKR" style="list-style-type: square; margin-left: 0; margin-right: 0; padding: 0;">
                  <li class="TYR86d wXCUfe zfr3Q" style="list-style-type: none;">
                   <ul class="n8H08c UVNKR" style="list-style-type: square; margin-left: 0; margin-right: 0; padding: 0;">
                    <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 30pt;">
                     <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.2; margin-left: 0; padding-left: 0; text-indent: 0;">
                      x position
                     </p>
                    </li>
                    <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 30pt;">
                     <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.2; margin-left: 0; padding-left: 0; text-indent: 0;">
                      y position
                     </p>
                    </li>
                    <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 30pt;">
                     <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.2; margin-left: 0; padding-left: 0; text-indent: 0;">
                      x velocity
                     </p>
                    </li>
                    <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 30pt;">
                     <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.2; margin-left: 0; padding-left: 0; text-indent: 0;">
                      y velocity
                     </p>
                    </li>
                    <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 30pt;">
                     <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.2; margin-left: 0; padding-left: 0; text-indent: 0;">
                      tilt angle
                     </p>
                    </li>
                    <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 30pt;">
                     <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.2; margin-left: 0; padding-left: 0; text-indent: 0;">
                      angular velocity
                     </p>
                    </li>
                    <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 30pt;">
                     <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.2; margin-left: 0; padding-left: 0; text-indent: 0;">
                      whether the right leg attaches to the ground (unused)
                     </p>
                    </li>
                    <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 30pt;">
                     <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.2; margin-left: 0; padding-left: 0; text-indent: 0;">
                      whether the left leg attaches to the ground (unused)
                     </p>
                    </li>
                   </ul>
                  </li>
                 </ul>
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.2; margin-left: 30pt; padding-left: 0; text-indent: 0;">
                  <br/>
                 </p>
                 <ul class="n8H08c UVNKR" style="list-style-type: square; margin-left: 0; margin-right: 0; padding: 0;">
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.2; margin-left: 0; padding-left: 0; text-indent: 0;">
                    <span style="font-family: 'Lato';">
                     <strong>
                      Action
                     </strong>
                    </span>
                   </p>
                  </li>
                 </ul>
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.2; margin-left: 15pt; padding-left: 0; text-indent: 0;">
                  The lunar land allows us to control the
                  <span style="font-family: 'Lato';">
                   <strong>
                    main engine
                   </strong>
                  </span>
                  and side engines. An action therefore consists of 2 dimensions, i.e.,
                 </p>
                 <ul class="n8H08c UVNKR" style="list-style-type: square; margin-left: 0; margin-right: 0; padding: 0;">
                  <li class="TYR86d wXCUfe zfr3Q" style="list-style-type: none;">
                   <ul class="n8H08c UVNKR" style="list-style-type: square; margin-left: 0; margin-right: 0; padding: 0;">
                    <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 30pt;">
                     <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.2; margin-left: 0; padding-left: 0; text-indent: 0;">
                      main engine power
                     </p>
                    </li>
                    <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 30pt;">
                     <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.2; margin-left: 0; padding-left: 0; text-indent: 0;">
                      side engine power
                     </p>
                    </li>
                   </ul>
                  </li>
                 </ul>
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.2; margin-left: 15pt; padding-left: 0; text-indent: 0;">
                  The main engine power and side engine power each consists of a real value in [−1, 1], indicating the thrust of the engines. For the main engine power, a value &lt; 0 stops the engine to produce thrust. For the side engine power, a negative value and a positive value refer to the left and right engine thrust, respectively.
                 </p>
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.2; margin-left: 15pt; padding-left: 0; text-indent: 0;">
                  <br/>
                 </p>
                 <ul class="n8H08c UVNKR" style="list-style-type: square; margin-left: 0; margin-right: 0; padding: 0;">
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.2; margin-left: 0; padding-left: 0; text-indent: 0;">
                    <span style="font-family: 'Lato';">
                     <strong>
                      Control Policy (Chromosome)
                     </strong>
                    </span>
                   </p>
                  </li>
                 </ul>
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.2; margin-left: 15pt; padding-left: 0; text-indent: 0;">
                  To establish a complete mapping between the observation and action spaces, a control policy must encode an action for each observation case. In other words, a control policy will be an 8192-dimensional vector (4^6 × 2), where each value is in [−1, 1]. You need to use GA to optimize the 8,192 thrust values for the lunar lander to gain as high reward as possible.
                 </p>
                </div>
               </div>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
        </div>
       </section>
       <section class="yaqOZd" id="h.12eabc9bace210f0_239" style="">
        <div class="IFuOkc">
        </div>
        <div class="mYVXT">
         <div class="LS81yb VICjCf" tabindex="-1">
          <div class="hJDwNd-AhqUyc-uQSCkd purZT-AhqUyc-II5mzb pSzOP-AhqUyc-qWD73c JNdkSc yYI8W">
           <div class="JNdkSc-SmKAyb">
            <div class="" jsaction="zXBUYb:zTPCnb;zQF9Uc:Qxe3nd;" jscontroller="sGwD4d" jsname="F57UId">
             <div class="oKdM2c Kzv0Me">
              <div class="hJDwNd-AhqUyc-uQSCkd jXK9ad D2fZ2 OjCsFc GNzUNc" id="h.12eabc9bace210f0_242">
               <div class="jXK9ad-SmKAyb">
                <div class="tyJCtd mGzaTb baZpAe">
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.38;">
                  <span class="jgG6ef" style="color: #226e93; font-variant: normal; vertical-align: baseline;">
                   Problem
                  </span>
                  <span class="jgG6ef" style="color: #226e93; vertical-align: baseline;">
                   Formulation
                  </span>
                 </p>
                </div>
               </div>
              </div>
             </div>
             <div class="oKdM2c">
              <div class="hJDwNd-AhqUyc-uQSCkd jXK9ad D2fZ2 wHaque" id="h.47af6d09445cb01b_59">
               <div class="jXK9ad-SmKAyb">
                <div class="tyJCtd OWlOyc baZpAe">
                 <div jsaction="rcuQ6b:rcuQ6b;" jscontroller="VYKRW">
                  <div class="WIdY2d M1aSXe">
                   <div jsname="WXxXjd" style="padding-top: 23.0107526882%">
                   </div>
                   <div class="YMEQtf">
                    <div class="w536ob" data-code="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
&lt;link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet'&gt;
&lt;style&gt;
body {
    font-family: 'Lato';font-size: 14.5px;
}
&lt;/style&gt;

&lt;script src=&quot;http://polyfill.io/v3/polyfill.min.js?features=es6&quot;&gt;&lt;/script&gt;
&lt;script type=&quot;text/javascript&quot; id=&quot;MathJax-script&quot; async
src=&quot;https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js&quot;&gt;
&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;p style=&quot;font-family: Lato&quot;&gt;This optimization problem can be formulated as
\[\mathop{\arg\max}\limits_{\boldsymbol{x}} f(\boldsymbol{x})\]
subject to 
\[\boldsymbol{x} \in [-1,1]^{8192},\]
where \(\boldsymbol{x}\) is the control policy and \(f:\mathbb{R}^{8192}\rightarrow\mathbb{R}\) is the evaluation (reward) function.
&lt;body&gt;
&lt;html&gt;" data-enable-interaction="true" data-url="https://1285915041-atari-embeds.googleusercontent.com/embeds/16cb204cf3a9d4d223a0a3fd8b0eec5d/inner-frame-minified.html" jsaction="rcuQ6b:WYd;" jscontroller="szRU7e" jsname="jkaScf">
                     <div class="EmVfjc qs41qe UzswCe" data-active="true" data-loadingmessage=" " jsaction="animationend:kWijWc;dyRcpb:dyRcpb" jscontroller="qAKInc" jsname="Hy6Uif">
                      <div aria-live="assertive" class="Cg7hO" jsname="vyyg5">
                      </div>
                      <div class="xu46lf" jsname="Hxlbvc">
                       <div class="ir3uv uWlRce co39ub">
                        <div class="xq3j6 ERcjC">
                         <div class="X6jHbb GOJTSe">
                         </div>
                        </div>
                        <div class="HBnAAc">
                         <div class="X6jHbb GOJTSe">
                         </div>
                        </div>
                        <div class="xq3j6 dj3yTd">
                         <div class="X6jHbb GOJTSe">
                         </div>
                        </div>
                       </div>
                       <div class="ir3uv GFoASc Cn087">
                        <div class="xq3j6 ERcjC">
                         <div class="X6jHbb GOJTSe">
                         </div>
                        </div>
                        <div class="HBnAAc">
                         <div class="X6jHbb GOJTSe">
                         </div>
                        </div>
                        <div class="xq3j6 dj3yTd">
                         <div class="X6jHbb GOJTSe">
                         </div>
                        </div>
                       </div>
                       <div class="ir3uv WpeOqd hfsr6b">
                        <div class="xq3j6 ERcjC">
                         <div class="X6jHbb GOJTSe">
                         </div>
                        </div>
                        <div class="HBnAAc">
                         <div class="X6jHbb GOJTSe">
                         </div>
                        </div>
                        <div class="xq3j6 dj3yTd">
                         <div class="X6jHbb GOJTSe">
                         </div>
                        </div>
                       </div>
                       <div class="ir3uv rHV3jf EjXFBf">
                        <div class="xq3j6 ERcjC">
                         <div class="X6jHbb GOJTSe">
                         </div>
                        </div>
                        <div class="HBnAAc">
                         <div class="X6jHbb GOJTSe">
                         </div>
                        </div>
                        <div class="xq3j6 dj3yTd">
                         <div class="X6jHbb GOJTSe">
                         </div>
                        </div>
                       </div>
                      </div>
                     </div>
                     <iframe aria-label="Custom embed" class="YMEQtf" frameborder="0" id="47af6d09445cb01b_59" jsname="WMhH6e" name="47af6d09445cb01b_59" sandbox="allow-scripts allow-popups allow-forms allow-same-origin allow-popups-to-escape-sandbox allow-downloads" scrolling="no" title="Custom embed">
                     </iframe>
                    </div>
                   </div>
                  </div>
                 </div>
                </div>
               </div>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
        </div>
       </section>
       <section class="yaqOZd cJgDec nyKByd" id="h.3362346e3d12c940_136" style="">
        <div class="IFuOkc" style="background-size: cover; background-position: center center; background-image: url(https://lh5.googleusercontent.com/ngNnjmJvuKzKj2xWj9Q7ohta9DM_5EYgy3gzkgqAFPD39M9oNIUHeceT2fwiGgS8TaHPNfzYhStSALr9feF77ws=w16383);">
        </div>
        <div class="mYVXT">
         <div class="LS81yb VICjCf" tabindex="-1">
          <div class="hJDwNd-AhqUyc-qWD73c purZT-AhqUyc-II5mzb pSzOP-AhqUyc-qWD73c JNdkSc yYI8W">
           <div class="JNdkSc-SmKAyb">
            <div class="" jsaction="zXBUYb:zTPCnb;zQF9Uc:Qxe3nd;" jscontroller="sGwD4d" jsname="F57UId">
             <div class="oKdM2c Kzv0Me">
              <div class="hJDwNd-AhqUyc-qWD73c jXK9ad D2fZ2 OjCsFc GNzUNc" id="h.12eabc9bace210f0_104">
               <div class="jXK9ad-SmKAyb">
                <div class="tyJCtd mGzaTb baZpAe">
                 <p class="CDt4Ke zfr3Q" dir="ltr">
                  <span style="font-variant: normal;">
                  </span>
                  <span class="RijTuc" style="color: #ffffff; font-family: 'Lato'; font-weight: 300; vertical-align: baseline;">
                   System Requirement
                  </span>
                 </p>
                </div>
               </div>
              </div>
             </div>
             <div class="oKdM2c">
              <div class="hJDwNd-AhqUyc-qWD73c jXK9ad D2fZ2 wHaque GNzUNc" id="h.3362346e3d12c940_20">
               <div class="jXK9ad-SmKAyb">
                <div class="tyJCtd mGzaTb baZpAe">
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="text-align: justify; white-space: normal;">
                  <span style="font-family: 'Lato'; font-size: 12pt; font-weight: normal; vertical-align: baseline;">
                   We will use the following Python libraries for this assignment, so make sure you have already installed Python 3.6+. If you use Python a lot for other projects, set up a new virtual environment is recommended.
                  </span>
                 </p>
                </div>
               </div>
              </div>
             </div>
            </div>
           </div>
          </div>
          <div class="hJDwNd-AhqUyc-qWD73c purZT-AhqUyc-II5mzb pSzOP-AhqUyc-qWD73c JNdkSc">
           <div class="JNdkSc-SmKAyb">
            <div class="" jsaction="zXBUYb:zTPCnb;zQF9Uc:Qxe3nd;" jscontroller="sGwD4d" jsname="F57UId">
             <div class="oKdM2c Kzv0Me">
              <div class="hJDwNd-AhqUyc-qWD73c jXK9ad D2fZ2 OjCsFc wHaque GNzUNc" id="h.12eabc9bace210f0_77">
               <div class="jXK9ad-SmKAyb">
                <div class="tyJCtd mGzaTb baZpAe">
                 <div class="CobnVe aP9Z7e" id="h.n6x4oqv4bicr">
                 </div>
                 <h2 class="CDt4Ke zfr3Q JYVBee" dir="ltr" id="h.n6x4oqv4bicr" style="background-color: transparent; border-bottom: none; border-left: none; border-right: none; border-top: none; line-height: 1.68; margin-bottom: 0; margin-top: 0; padding-bottom: 0; padding-left: 0; padding-right: 0; padding-top: 0;" tabindex="-1">
                  <div class="CjVfdc" jsaction="touchstart:UrsOsc; click:KjsqPd; focusout:QZoaZ; mouseover:y0pDld; mouseout:dq0hvd;fv1Rjc:jbFSOd;CrfLRd:SzACGe;" jscontroller="Ae65rd">
                   <div class="PPhIP rviiZ" jsname="haAclf">
                    <div aria-describedby="h.n6x4oqv4bicr" aria-disabled="false" aria-hidden="true" aria-label="Copy heading link" class="U26fgb mUbCce fKz7Od LRAOtb Znu9nd M9Bg4d" data-tooltip="Copy heading link" data-tooltip-horizontal-offset="0" data-tooltip-position="top" data-tooltip-vertical-offset="12" jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue; focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef;" jscontroller="mxS5xe" jsshadow="" role="presentation">
                     <a aria-describedby="h.n6x4oqv4bicr" aria-label="Copy heading link" class="FKF6mc TpQm9d" href="#h.n6x4oqv4bicr" jsname="hiK3ld" role="button">
                      <div class="VTBa7b MbhUzd" jsname="ksKsZd">
                      </div>
                      <span class="xjKiLb" jsslot="">
                       <span class="Ce1Y1c" style="top: -11px">
                        <svg class="OUGEr QdAdhf" fill="currentColor" focusable="false" height="22px" viewbox="0 0 24 24" width="22px">
                         <path d="M0 0h24v24H0z" fill="none">
                         </path>
                         <path d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z">
                         </path>
                        </svg>
                       </span>
                      </span>
                     </a>
                    </div>
                   </div>
                   <span class="jgG6ef" style="color: #ffffff; font-family: 'Lato'; font-weight: normal; vertical-align: baseline;">
                    Windows 10
                   </span>
                  </div>
                 </h2>
                 <ul class="n8H08c UVNKR" style="list-style-type: square; margin-left: 0; margin-right: 0; padding: 0;">
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="background-clip: padding-box; background-color: rgba(0,0,0,0.059); border-bottom: none; border-left: 0.75pt solid rgba(255,255,255,0.122); border-right: 0.75pt solid rgba(255,255,255,0.122); border-top: 0.75pt solid rgba(255,255,255,0.122); margin-bottom: 0; margin-left: 0; margin-top: 0; padding-bottom: 0; padding-left: 4pt; padding-right: 4pt; padding-top: 4pt; text-indent: 0;">
                    <span style="color: #ffffff; font-family: 'Source Code Pro'; font-size: 12pt; font-weight: normal; vertical-align: baseline;">
                     pip install gym
                    </span>
                   </p>
                  </li>
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="background-clip: padding-box; background-color: rgba(0,0,0,0.059); border-bottom: none; border-left: 0.75pt solid rgba(255,255,255,0.122); border-right: 0.75pt solid rgba(255,255,255,0.122); border-top: none; margin-bottom: 0; margin-left: 0; margin-top: 0; padding-bottom: 0; padding-left: 4pt; padding-right: 4pt; padding-top: 0; text-indent: 0;">
                    <span style="color: #ffffff; font-family: 'Source Code Pro'; font-size: 12pt; font-weight: normal; vertical-align: baseline;">
                     pip install box2d
                    </span>
                   </p>
                  </li>
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="background-clip: padding-box; background-color: rgba(0,0,0,0.059); border-bottom: 0.75pt solid rgba(255,255,255,0.122); border-left: 0.75pt solid rgba(255,255,255,0.122); border-right: 0.75pt solid rgba(255,255,255,0.122); border-top: none; margin-bottom: 0; margin-left: 0; margin-top: 0; padding-bottom: 4pt; padding-left: 4pt; padding-right: 4pt; padding-top: 0; text-indent: 0;">
                    <span style="color: #ffffff; font-family: 'Source Code Pro'; font-size: 12pt; font-weight: normal; vertical-align: baseline;">
                     pip install pyglet
                    </span>
                   </p>
                  </li>
                 </ul>
                 <div class="CobnVe aP9Z7e" id="h.k9yvkn15ses">
                 </div>
                 <h2 class="CDt4Ke zfr3Q JYVBee" dir="ltr" id="h.k9yvkn15ses" style="background-color: transparent; border-bottom: none; border-left: none; border-right: none; border-top: none; line-height: 1.68; margin-bottom: 0; margin-top: 0; padding-bottom: 0; padding-left: 0; padding-right: 0; padding-top: 0;">
                  <br/>
                 </h2>
                 <div class="CobnVe aP9Z7e" id="h.q0n1j7izswjg">
                 </div>
                 <h2 class="CDt4Ke zfr3Q JYVBee" dir="ltr" id="h.q0n1j7izswjg" style="background-color: transparent; border-bottom: none; border-left: none; border-right: none; border-top: none; line-height: 1.68; margin-bottom: 0; margin-top: 0; padding-bottom: 0; padding-left: 0; padding-right: 0; padding-top: 0;" tabindex="-1">
                  <div class="CjVfdc" jsaction="touchstart:UrsOsc; click:KjsqPd; focusout:QZoaZ; mouseover:y0pDld; mouseout:dq0hvd;fv1Rjc:jbFSOd;CrfLRd:SzACGe;" jscontroller="Ae65rd">
                   <div class="PPhIP rviiZ" jsname="haAclf">
                    <div aria-describedby="h.q0n1j7izswjg" aria-disabled="false" aria-hidden="true" aria-label="Copy heading link" class="U26fgb mUbCce fKz7Od LRAOtb Znu9nd M9Bg4d" data-tooltip="Copy heading link" data-tooltip-horizontal-offset="0" data-tooltip-position="top" data-tooltip-vertical-offset="12" jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue; focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef;" jscontroller="mxS5xe" jsshadow="" role="presentation">
                     <a aria-describedby="h.q0n1j7izswjg" aria-label="Copy heading link" class="FKF6mc TpQm9d" href="#h.q0n1j7izswjg" jsname="hiK3ld" role="button">
                      <div class="VTBa7b MbhUzd" jsname="ksKsZd">
                      </div>
                      <span class="xjKiLb" jsslot="">
                       <span class="Ce1Y1c" style="top: -11px">
                        <svg class="OUGEr QdAdhf" fill="currentColor" focusable="false" height="22px" viewbox="0 0 24 24" width="22px">
                         <path d="M0 0h24v24H0z" fill="none">
                         </path>
                         <path d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z">
                         </path>
                        </svg>
                       </span>
                      </span>
                     </a>
                    </div>
                   </div>
                   <span class="jgG6ef" style="color: #ffffff; vertical-align: baseline;">
                    m
                   </span>
                   <span class="jgG6ef" style="color: #ffffff; font-family: 'Lato'; font-variant: normal; font-weight: normal; vertical-align: baseline;">
                    acOS
                   </span>
                  </div>
                 </h2>
                 <ul class="n8H08c UVNKR" style="list-style-type: square; margin-left: 0; margin-right: 0; padding: 0;">
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="background-clip: padding-box; background-color: rgba(0,0,0,0.059); border-bottom: none; border-left: 0.75pt solid rgba(255,255,255,0.122); border-right: 0.75pt solid rgba(255,255,255,0.122); border-top: 0.75pt solid rgba(255,255,255,0.122); margin-bottom: 0; margin-left: 0; margin-top: 0; padding-bottom: 0; padding-left: 4pt; padding-right: 4pt; padding-top: 4pt; text-indent: 0;">
                    <span style="color: #ffffff; font-family: 'Source Code Pro'; font-size: 12pt; font-variant: normal; font-weight: normal; vertical-align: baseline;">
                     pip3 install gym[all]
                    </span>
                   </p>
                  </li>
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="background-clip: padding-box; background-color: rgba(0,0,0,0.059); border-bottom: 0.75pt solid rgba(255,255,255,0.122); border-left: 0.75pt solid rgba(255,255,255,0.122); border-right: 0.75pt solid rgba(255,255,255,0.122); border-top: none; margin-bottom: 0; margin-left: 0; margin-top: 0; padding-bottom: 4pt; padding-left: 4pt; padding-right: 4pt; padding-top: 0; text-indent: 0;">
                    <span style="color: #ffffff; font-family: 'Source Code Pro'; font-size: 12pt; font-variant: normal; font-weight: normal; vertical-align: baseline;">
                     pip3 install box2d
                    </span>
                   </p>
                  </li>
                 </ul>
                 <p class="CDt4Ke zfr3Q" dir="ltr">
                  <br/>
                 </p>
                 <p class="CDt4Ke zfr3Q" dir="ltr">
                  <span style="font-family: 'Lato'; font-size: 12pt; font-weight: normal; vertical-align: baseline;">
                   You can run
                  </span>
                  <span style="background-color: rgba(0,0,0,0.059); color: #ffffff; font-family: 'Source Code Pro'; font-variant: normal;">
                   <strong>
                    LunarLander_HW.py
                   </strong>
                  </span>
                  <span style="font-family: 'Lato'; font-size: 12pt; font-weight: normal; vertical-align: baseline;">
                  </span>
                  <span style="font-family: 'Lato'; font-size: 12pt; font-variant: normal; font-weight: normal; vertical-align: baseline;">
                   af
                  </span>
                  <span style="color: #ffffff; font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                   ter successfully installed the above packages.
                  </span>
                 </p>
                </div>
               </div>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
        </div>
       </section>
       <section class="yaqOZd" id="h.12eabc9bace210f0_172" style="">
        <div class="IFuOkc">
        </div>
        <div class="mYVXT">
         <div class="LS81yb VICjCf" tabindex="-1">
          <div class="hJDwNd-AhqUyc-uQSCkd purZT-AhqUyc-II5mzb pSzOP-AhqUyc-qWD73c JNdkSc">
           <div class="JNdkSc-SmKAyb">
            <div class="" jsaction="zXBUYb:zTPCnb;zQF9Uc:Qxe3nd;" jscontroller="sGwD4d" jsname="F57UId">
             <div class="oKdM2c Kzv0Me">
              <div class="hJDwNd-AhqUyc-uQSCkd jXK9ad D2fZ2 OjCsFc wHaque GNzUNc" id="h.12eabc9bace210f0_169">
               <div class="jXK9ad-SmKAyb">
                <div class="tyJCtd mGzaTb baZpAe">
                 <p class="CDt4Ke zfr3Q" dir="ltr">
                  <span class="RijTuc" style="color: #226e93; font-family: 'Lato'; font-weight: 300; vertical-align: baseline;">
                   A
                  </span>
                  <span class="RijTuc" style="color: #226e93; font-family: 'Lato'; font-variant: normal; font-weight: 300; vertical-align: baseline;">
                   bout
                  </span>
                  <span class="RijTuc" style="color: #226e93; font-family: 'Lato'; font-weight: 300; vertical-align: baseline;">
                   T
                  </span>
                  <span class="RijTuc" style="color: #226e93; font-family: 'Lato'; font-variant: normal; font-weight: 300; vertical-align: baseline;">
                   he
                  </span>
                  <span class="RijTuc" style="color: #226e93; font-family: 'Lato'; font-weight: 300; vertical-align: baseline;">
                   A
                  </span>
                  <span class="RijTuc" style="color: #226e93; font-family: 'Lato'; font-variant: normal; font-weight: 300; vertical-align: baseline;">
                   ssignments
                  </span>
                 </p>
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.38;">
                  <span class="jgG6ef" style="color: #226e93; font-family: 'Lato'; font-variant: normal; font-weight: normal; vertical-align: baseline;">
                   Crossover
                  </span>
                 </p>
                 <p class="CDt4Ke zfr3Q" dir="ltr">
                  <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                   Please implement your crossover operation in the
                  </span>
                  <span style="background-color: rgba(0,0,0,0.059); font-family: 'Source Code Pro'; font-variant: normal; font-weight: normal;">
                   crossover(cls, parent1, parent2, xover rate)
                  </span>
                  <span style="background-color: rgba(0,0,0,0.059); font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                  </span>
                  <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                   function.
                  </span>
                 </p>
                 <ul class="n8H08c UVNKR" style="list-style-type: square; margin-left: 0; margin-right: 0; padding: 0;">
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="margin-left: 0; padding-left: 0; text-indent: 0;">
                    <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                     Arguments:
                    </span>
                    <span style="background-color: rgba(0,0,0,0.059); font-family: 'Source Code Pro'; font-variant: normal; font-weight: normal;">
                     parent1 (Chromosome)
                    </span>
                    <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                     ,
                    </span>
                    <span style="background-color: rgba(0,0,0,0.059); font-family: 'Source Code Pro'; font-variant: normal; font-weight: normal;">
                     parent2 (Chromosome)
                    </span>
                    <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                     ,
                    </span>
                    <span style="background-color: rgba(0,0,0,0.059); font-family: 'Source Code Pro'; font-variant: normal; font-weight: normal;">
                     xover rate (float)
                    </span>
                   </p>
                  </li>
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="margin-left: 0; padding-left: 0; text-indent: 0;">
                    <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                     Return: Two children in a tuple, i.e.,
                    </span>
                    <span style="background-color: rgba(0,0,0,0.059); font-family: 'Source Code Pro'; font-variant: normal; font-weight: normal;">
                     (child1, child2)
                    </span>
                    <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                     ; each child is an instance of
                    </span>
                    <span style="background-color: rgba(0,0,0,0.059); font-family: 'Source Code Pro'; font-variant: normal; font-weight: normal;">
                     Chromosome
                    </span>
                    <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                     .
                    </span>
                   </p>
                  </li>
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="margin-left: 0; padding-left: 0; text-indent: 0;">
                    <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                     Boundary: All the genetic values should be bounded in [−1, 1] .
                    </span>
                   </p>
                  </li>
                 </ul>
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.38;">
                  <span class="jgG6ef" style="color: #226e93; font-family: 'Lato'; font-variant: normal; font-weight: normal; vertical-align: baseline;">
                   Mutation
                  </span>
                 </p>
                 <p class="CDt4Ke zfr3Q" dir="ltr">
                  <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                   Please implement your crossover operation in the
                  </span>
                  <span style="background-color: rgba(0,0,0,0.059); font-family: 'Source Code Pro'; font-variant: normal; font-weight: normal;">
                   mutate(cls, chrm, mutate rate)
                  </span>
                  <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                   function.
                  </span>
                 </p>
                 <ul class="n8H08c UVNKR" style="list-style-type: square; margin-left: 0; margin-right: 0; padding: 0;">
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="margin-left: 0; padding-left: 0; text-indent: 0;">
                    <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                     Arguments:
                    </span>
                    <span style="background-color: rgba(0,0,0,0.059); font-family: 'Source Code Pro'; font-variant: normal; font-weight: normal;">
                     chrm (Chromosome)
                    </span>
                    <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                     ,
                    </span>
                    <span style="background-color: rgba(0,0,0,0.059); font-family: 'Source Code Pro'; font-variant: normal; font-weight: normal;">
                     mutate rate (float)
                    </span>
                    <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                    </span>
                   </p>
                  </li>
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="margin-left: 0; padding-left: 0; text-indent: 0;">
                    <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                     Return:
                    </span>
                    <span style="background-color: rgba(0,0,0,0.059); font-family: 'Source Code Pro'; font-variant: normal; font-weight: normal;">
                     None
                    </span>
                   </p>
                  </li>
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="margin-left: 0; padding-left: 0; text-indent: 0;">
                    <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                     Boundary: All the genetic values should be bounded in [−1, 1] .
                    </span>
                   </p>
                  </li>
                 </ul>
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.38;">
                  <span class="jgG6ef" style="color: #226e93; font-family: 'Lato'; font-variant: normal; font-weight: normal; vertical-align: baseline;">
                   k - tournament selection
                  </span>
                 </p>
                 <p class="CDt4Ke zfr3Q" dir="ltr">
                  <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                   Please implement the k-tournament selection in the
                  </span>
                  <span style="background-color: rgba(0,0,0,0.059); font-family: 'Source Code Pro'; font-variant: normal; font-weight: normal;">
                   parent selection(self, k)
                  </span>
                  <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                   function.
                  </span>
                 </p>
                 <ul class="n8H08c UVNKR" style="list-style-type: square; margin-left: 0; margin-right: 0; padding: 0;">
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="margin-left: 0; padding-left: 0; text-indent: 0;">
                    <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                     Arguments:
                    </span>
                    <span style="background-color: rgba(0,0,0,0.059); font-family: 'Source Code Pro'; font-variant: normal; font-weight: normal;">
                     self (GA)
                    </span>
                    <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                     ,
                    </span>
                    <span style="background-color: rgba(0,0,0,0.059); font-family: 'Source Code Pro'; font-variant: normal; font-weight: normal;">
                     k (int)
                    </span>
                   </p>
                  </li>
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="margin-left: 0; padding-left: 0; text-indent: 0;">
                    <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                     Return: a selected
                    </span>
                    <span style="background-color: rgba(0,0,0,0.059); font-family: 'Source Code Pro'; font-variant: normal; font-weight: normal;">
                     parent (Chromosome)
                    </span>
                   </p>
                  </li>
                 </ul>
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.38;">
                  <span class="jgG6ef" style="color: #226e93; font-family: 'Lato'; font-variant: normal; font-weight: normal; vertical-align: baseline;">
                   GA parameters
                  </span>
                 </p>
                 <ul class="n8H08c UVNKR" style="list-style-type: square; margin-left: 0; margin-right: 0; padding: 0;">
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="margin-left: 0; padding-left: 0; text-indent: 0;">
                    <span style="font-family: 'Lato'; font-variant: normal; font-weight: normal;">
                     Please try different GA parameters and report an appropriate setting for this problem.
                    </span>
                   </p>
                  </li>
                 </ul>
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.38;">
                  <span class="jgG6ef" style="color: #226e93; vertical-align: baseline;">
                   Simulation times (Optional)
                  </span>
                 </p>
                 <ul class="n8H08c UVNKR" style="list-style-type: square; margin-left: 0; margin-right: 0; padding: 0;">
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="margin-left: 0; padding-left: 0; text-indent: 0;">
                    <span style="background-color: rgba(0,0,0,0.059); font-family: 'Source Code Pro'; font-variant: normal; font-weight: normal;">
                     SIMULATIONS_PER_EVALUTION
                    </span>
                    <span style="color: #000000; font-variant: normal;">
                    </span>
                    <span style="color: #000000;">
                     controls the simulation times in one evaluation.
                    </span>
                   </p>
                  </li>
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="background-color: transparent; border-bottom: none; border-left: none; border-right: none; border-top: none; line-height: 1.6285714285714286; margin-bottom: 0; margin-left: 0; margin-top: 0; padding-bottom: 0; padding-left: 0; padding-right: 0; padding-top: 0; text-indent: 0;">
                    <span style="color: #000000;">
                     Since the simulation environment is randomly generated, the simulation should be run several times to get the reliable performance.
                    </span>
                   </p>
                  </li>
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="background-color: transparent; border-bottom: none; border-left: none; border-right: none; border-top: none; line-height: 1.6285714285714286; margin-bottom: 0; margin-left: 0; margin-top: 0; padding-bottom: 0; padding-left: 0; padding-right: 0; padding-top: 0; text-indent: 0;">
                    <span style="color: #000000;">
                     Lowering simulation times makes the whole GA run faster, which gives you the sense of how different parameters affect the performance.
                    </span>
                   </p>
                  </li>
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="background-color: transparent; border-bottom: none; border-left: none; border-right: none; border-top: none; line-height: 1.6285714285714286; margin-bottom: 0; margin-left: 0; margin-top: 0; padding-bottom: 0; padding-left: 0; padding-right: 0; padding-top: 0; text-indent: 0;">
                    <span style="color: #000000;">
                     I
                    </span>
                    <span style="color: #000000;">
                     t is suggested that you set it to 15 to get a reliable output for homework assignment.
                    </span>
                   </p>
                  </li>
                 </ul>
                </div>
               </div>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
        </div>
       </section>
       <section class="yaqOZd qeLZfd" id="h.2cd9f4e78e5575fc_0" style="">
        <div class="IFuOkc">
        </div>
        <div class="mYVXT">
         <div class="LS81yb VICjCf" tabindex="-1">
          <div class="hJDwNd-AhqUyc-uQSCkd purZT-AhqUyc-II5mzb pSzOP-AhqUyc-qWD73c JNdkSc yYI8W">
           <div class="JNdkSc-SmKAyb">
            <div class="" jsaction="zXBUYb:zTPCnb;zQF9Uc:Qxe3nd;" jscontroller="sGwD4d" jsname="F57UId">
             <div class="oKdM2c Kzv0Me">
              <div class="hJDwNd-AhqUyc-uQSCkd jXK9ad D2fZ2 OjCsFc GNzUNc" id="h.344a5156fa92aa0d_17">
               <div class="jXK9ad-SmKAyb">
                <div class="tyJCtd mGzaTb baZpAe">
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.38;">
                  <span class="jgG6ef" style="color: #226e93; font-family: 'Lato'; font-variant: normal; font-weight: normal; vertical-align: baseline;">
                   R
                  </span>
                  <span class="jgG6ef" style="color: #226e93; vertical-align: baseline;">
                   eport
                  </span>
                 </p>
                 <ul class="n8H08c UVNKR" style="list-style-type: square; margin-left: 0; margin-right: 0; padding: 0;">
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="background-color: transparent; border-bottom: none; border-left: none; border-right: none; border-top: none; line-height: 1.38; margin-bottom: 0; margin-left: 0; margin-top: 10pt; padding-bottom: 0; padding-left: 0; padding-right: 0; padding-top: 0; text-indent: 0;">
                    <span style="font-family: 'Arial'; font-weight: normal;">
                     Describe your methods and list their parameter settings for the experiments.
                    </span>
                   </p>
                  </li>
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="background-color: transparent; border-bottom: none; border-left: none; border-right: none; border-top: none; line-height: 1.38; margin-bottom: 0; margin-left: 0; margin-top: 10pt; padding-bottom: 0; padding-left: 0; padding-right: 0; padding-top: 0; text-indent: 0;">
                    <span style="font-family: 'Arial'; font-weight: normal;">
                     Present the experimental results:
                    </span>
                   </p>
                   <ul class="n8H08c UVNKR" style="list-style-type: square; margin-left: 0; margin-right: 0; padding: 0;">
                    <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                     <p class="CDt4Ke zfr3Q" dir="ltr" style="background-color: transparent; border-bottom: none; border-left: none; border-right: none; border-top: none; line-height: 1.38; margin-bottom: 0; margin-left: 0; margin-top: 10pt; padding-bottom: 0; padding-left: 0; padding-right: 0; padding-top: 0; text-indent: 0;">
                      <span style="font-family: 'Arial'; font-variant: normal; font-weight: normal;">
                       List all the fitness values obtained.
                      </span>
                     </p>
                    </li>
                    <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                     <p class="CDt4Ke zfr3Q" dir="ltr" style="background-color: transparent; border-bottom: none; border-left: none; border-right: none; border-top: none; line-height: 1.38; margin-bottom: 0; margin-left: 0; margin-top: 10pt; padding-bottom: 0; padding-left: 0; padding-right: 0; padding-top: 0; text-indent: 0;">
                      <span style="font-family: 'Arial'; font-variant: normal; font-weight: normal;">
                       Draw the anytime behavior.
                      </span>
                     </p>
                    </li>
                   </ul>
                  </li>
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="background-color: transparent; border-bottom: none; border-left: none; border-right: none; border-top: none; line-height: 1.38; margin-bottom: 0; margin-left: 0; margin-top: 10pt; padding-bottom: 0; padding-left: 0; padding-right: 0; padding-top: 0; text-indent: 0;">
                    <span style="font-family: 'Arial'; font-weight: normal;">
                     Try different operators and parameter settings, and compare their results.
                    </span>
                   </p>
                  </li>
                 </ul>
                </div>
               </div>
              </div>
             </div>
             <div class="oKdM2c">
              <div class="hJDwNd-AhqUyc-uQSCkd jXK9ad D2fZ2 GNzUNc" id="h.12eabc9bace210f0_159">
               <div class="jXK9ad-SmKAyb">
                <div class="tyJCtd mGzaTb baZpAe">
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.38;">
                  <span class="jgG6ef" style="color: #226e93; font-family: 'Lato'; font-weight: normal; vertical-align: baseline;">
                   Submission
                  </span>
                 </p>
                 <ul class="n8H08c UVNKR" style="list-style-type: square; margin-left: 0; margin-right: 0; padding: 0;">
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="background-color: transparent; border-bottom: none; border-left: none; border-right: none; border-top: none; line-height: 1.2; margin-bottom: 0; margin-left: 0; margin-top: 10pt; padding-bottom: 0; padding-left: 0; padding-right: 0; padding-top: 0; text-indent: 0;">
                    <span style="color: #212121;">
                     Please zip
                    </span>
                    <span style="color: #212121;">
                     the
                    </span>
                    <span style="color: #212121; font-family: 'Lato';">
                     <strong>
                      source code (
                     </strong>
                    </span>
                    <span style="background-color: rgba(0,0,0,0.059); color: #212121; font-family: 'Source Code Pro'; font-variant: normal;">
                     <strong>
                      studentID_LunarLander_HW.py
                     </strong>
                    </span>
                    <span style="color: #212121; font-family: 'Lato';">
                     <strong>
                      )
                     </strong>
                    </span>
                    <span style="color: #212121;">
                     and
                    </span>
                    <span style="color: #212121; font-family: 'Lato';">
                     <strong>
                      report
                     </strong>
                    </span>
                    <span style="color: #212121; font-family: 'Lato'; font-variant: normal;">
                     <strong>
                      (
                     </strong>
                    </span>
                    <span style="background-color: rgba(0,0,0,0.059); color: #212121; font-family: 'Source Code Pro'; font-variant: normal;">
                     <strong>
                      studentID.p
                     </strong>
                    </span>
                    <span style="background-color: rgba(0,0,0,0.059); color: #212121; font-family: 'Source Code Pro';">
                     <strong>
                      df
                     </strong>
                    </span>
                    <span style="color: #212121; font-family: 'Lato'; font-variant: normal;">
                     <strong>
                      )
                     </strong>
                    </span>
                    <span style="color: #212121;">
                     . U
                    </span>
                    <span style="color: #212121; font-family: 'Lato'; font-weight: normal;">
                     pload
                    </span>
                    <span style="color: #212121;">
                     it
                    </span>
                    <span style="color: #212121; font-family: 'Lato'; font-weight: normal;">
                     to eeclass.
                    </span>
                   </p>
                  </li>
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="background-color: transparent; border-bottom: none; border-left: none; border-right: none; border-top: none; line-height: 1.2; margin-bottom: 0; margin-left: 0; margin-top: 15pt; padding-bottom: 0; padding-left: 0; padding-right: 0; padding-top: 0; text-indent: 0;">
                    <span style="color: #212121; font-family: 'Lato'; font-weight: normal;">
                     All unexpected files will be ignore when testing and scoring.
                    </span>
                   </p>
                  </li>
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="background-color: transparent; border-bottom: none; border-left: none; border-right: none; border-top: none; line-height: 1.2; margin-bottom: 0; margin-left: 0; margin-top: 15pt; padding-bottom: 0; padding-left: 0; padding-right: 0; padding-top: 0; text-indent: 0;">
                    <span style="color: #212121; font-family: 'Lato'; font-weight: normal;">
                     Remove/comment out your debugging code snippets before submitting.
                    </span>
                   </p>
                  </li>
                 </ul>
                </div>
               </div>
              </div>
             </div>
             <div class="oKdM2c">
              <div class="hJDwNd-AhqUyc-uQSCkd jXK9ad D2fZ2 wHaque GNzUNc" id="h.633ab368c9aa1636_0">
               <div class="jXK9ad-SmKAyb">
                <div class="tyJCtd mGzaTb baZpAe">
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.38;">
                  <span class="jgG6ef" style="color: #226e93; font-family: 'Lato'; font-variant: normal; font-weight: normal; vertical-align: baseline;">
                   Sou
                  </span>
                  <span class="jgG6ef" style="color: #226e93; vertical-align: baseline;">
                   rce code
                  </span>
                 </p>
                 <ul class="n8H08c UVNKR" style="list-style-type: square; margin-left: 0; margin-right: 0; padding: 0;">
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="background-color: transparent; border-bottom: none; border-left: none; border-right: none; border-top: none; line-height: 1.2; margin-bottom: 0; margin-left: 0; margin-top: 15pt; padding-bottom: 0; padding-left: 0; padding-right: 0; padding-top: 0; text-indent: 0;">
                    <span class="aw5Odc" style="text-decoration: underline;">
                     <a class="XqQF9c" href="https://drive.google.com/file/d/1Zlk7V5CCAp5_f5eR__CS58q9puE1lK7F/view?usp=sharing" target="_blank">
                      Download
                     </a>
                    </span>
                    <span style="color: #212121;">
                    </span>
                   </p>
                  </li>
                 </ul>
                </div>
               </div>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
        </div>
       </section>
       <section class="yaqOZd" id="h.344a5156fa92aa0d_20" style="">
        <div class="IFuOkc">
        </div>
        <div class="mYVXT">
         <div class="LS81yb VICjCf" tabindex="-1">
          <div class="hJDwNd-AhqUyc-uQSCkd purZT-AhqUyc-II5mzb pSzOP-AhqUyc-qWD73c JNdkSc">
           <div class="JNdkSc-SmKAyb">
            <div class="" jsaction="zXBUYb:zTPCnb;zQF9Uc:Qxe3nd;" jscontroller="sGwD4d" jsname="F57UId">
             <div class="oKdM2c Kzv0Me">
              <div class="hJDwNd-AhqUyc-uQSCkd jXK9ad D2fZ2 OjCsFc wHaque GNzUNc" id="h.12eabc9bace210f0_188">
               <div class="jXK9ad-SmKAyb">
                <div class="tyJCtd mGzaTb baZpAe">
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.38;">
                  <span class="jgG6ef" style="color: #226e93; font-family: 'Lato'; font-weight: normal; vertical-align: baseline;">
                   References
                  </span>
                 </p>
                 <ul class="n8H08c UVNKR" style="list-style-type: square; margin-left: 0; margin-right: 0; padding: 0;">
                  <li class="TYR86d wXCUfe zfr3Q" dir="ltr" style="margin-left: 15pt;">
                   <p class="CDt4Ke zfr3Q" dir="ltr" style="background-color: transparent; border-bottom: none; border-left: none; border-right: none; border-top: none; line-height: 1.38; margin-bottom: 0; margin-left: 0; margin-top: 10pt; padding-bottom: 0; padding-left: 0; padding-right: 0; padding-top: 0; text-indent: 0;">
                    <span class="aw5Odc" style="font-family: 'Arial'; font-weight: normal; text-decoration: underline;">
                     <a class="XqQF9c" href="https://www.google.com/url?q=https%3A%2F%2Fgym.openai.com%2Fenvs%2FLunarLanderContinuous-v2%2F&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNE7YNQW8m48NdtIL8b3ROkb_kYVfA" target="_blank">
                      Gym (openai.com)
                     </a>
                    </span>
                    <span style="color: #000000; font-family: 'Arial'; font-weight: normal;">
                    </span>
                   </p>
                  </li>
                 </ul>
                </div>
               </div>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
        </div>
       </section>
      </div>
      <div class="Xpil1b">
      </div>
      <footer>
       <section class="yaqOZd" id="h.12fce10e77be29fa_28" style="">
        <div class="IFuOkc">
        </div>
        <div class="mYVXT">
         <div class="LS81yb VICjCf" tabindex="-1">
          <div class="hJDwNd-AhqUyc-uQSCkd purZT-AhqUyc-II5mzb pSzOP-AhqUyc-qWD73c JNdkSc">
           <div class="JNdkSc-SmKAyb">
            <div class="" jsaction="zXBUYb:zTPCnb;zQF9Uc:Qxe3nd;" jscontroller="sGwD4d" jsname="F57UId">
             <div class="oKdM2c Kzv0Me">
              <div class="hJDwNd-AhqUyc-uQSCkd jXK9ad D2fZ2 OjCsFc wHaque GNzUNc" id="h.12fce10e77be29fa_25">
               <div class="jXK9ad-SmKAyb">
                <div class="tyJCtd mGzaTb baZpAe">
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="line-height: 1.44;">
                  <span style="color: #212121; font-family: 'Lato'; font-size: 9pt; font-weight: normal; vertical-align: baseline;">
                   This site is composed by Heng-An Chen, Yi-Reui Chen,
                  </span>
                  <span style="color: #212121; font-size: 9pt; vertical-align: baseline;">
                   Yu-Wei Wen
                  </span>
                  <span style="color: #000000; font-family: 'Arial'; font-weight: normal;">
                  </span>
                  <span style="color: #212121; font-family: 'Lato'; font-size: 9pt; font-weight: normal; vertical-align: baseline;">
                   . Last update 2020.11.
                  </span>
                  <span style="color: #212121; font-size: 9pt; vertical-align: baseline;">
                   04
                  </span>
                 </p>
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="background-color: transparent; border-bottom: none; border-left: none; border-right: none; border-top: none; line-height: 1.44; margin-bottom: 0; margin-top: 0; padding-bottom: 0; padding-left: 0; padding-right: 0; padding-top: 0;">
                  <span style="color: #212121; font-family: 'Lato'; font-size: 9pt; font-weight: normal; vertical-align: baseline;">
                   Computational Intelligence Lab (CI Lab), Dept. of PME, NTHU, Taiwan.
                  </span>
                 </p>
                 <p class="CDt4Ke zfr3Q" dir="ltr" style="text-align: center;">
                  <br/>
                 </p>
                </div>
               </div>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
        </div>
       </section>
      </footer>
      <div class="dZA9kd ynRLnc" data-last-updated-at-time="1636006694073" jsaction="rcuQ6b:rcuQ6b;MxH79b:JdcaS;FaOgy:XuHpsb;" jscontroller="j1RDQb">
       <div aria-disabled="false" aria-expanded="false" aria-haspopup="true" aria-label="Site actions" class="U26fgb JRtysb WzwrXb I12f0b K2mXPb zXBiaf ynRLnc" data-anchor-corner="top-start" data-menu-corner="bottom-start" jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue; focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef;touchstart:p6p2H; touchmove:FwuNnf; touchend:yfqBxc(preventMouseEvents=true|preventDefault=true); touchcancel:JMtRjd;;keydown:I481le;" jscontroller="iSvg6e" jsname="Bg3gkf" jsshadow="" role="button" tabindex="0">
        <div class="NWlf3e MbhUzd" jsname="ksKsZd">
        </div>
        <span class="MhXXcc oJeWuf" jsslot="">
         <span class="Lw7GHd snByac">
          <svg class="NMm5M" focusable="false" height="24" viewbox="0 0 24 24" width="24">
           <path d="M11 17h2v-6h-2v6zm1-15C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zM11 9h2V7h-2v2z">
           </path>
          </svg>
         </span>
        </span>
        <div aria-hidden="true" jsname="xl07Ob" style="display:none">
         <div class="JPdR6b hVNH5c" jsaction="IpSVtb:TvD9Pc;fEN2Ze:xzS4ub;frq95c:LNeFm;cFpp9e:J9oOtd; click:H8nU8b; mouseup:H8nU8b; keydown:I481le; keypress:Kr2w4b; blur:O22p3e; focus:H8nU8b" jscontroller="uY3Nvd" role="menu" style="position:fixed" tabindex="0">
          <div class="XvhY1d" jsaction="mousedown:p8EH2c; touchstart:p8EH2c;">
           <div class="JAPqpe K0NPx">
            <span aria-label="Report abuse" class="z80M1 FeRvI" data-disabled-tooltip="Report abuse is not available in preview mode" jsaction="click:o6ZaF(preventDefault=true); mousedown:lAhnzb; mouseup:Osgxgf; mouseenter:SKyDAe; mouseleave:xq3APb;touchstart:jJiBRc; touchmove:kZeBdd; touchend:VfAz8(preventMouseEvents=true)" jsname="j7LFlb" jsslot="" role="menuitem" tabindex="-1">
             <div class="aBBjbd MbhUzd" jsname="ksKsZd">
             </div>
             <div class="uyYuVb oJeWuf" data-abuse-proto='%.@.null,null,"https://sites.google.com/gapp.nthu.edu.tw/lunarlander-ga",null,null,[],[]]' jsaction="JIbuQc:dQ6O0c;" jscontroller="HYv29e" jsname="xx9PJb">
              <div class="jO7h3c">
               Report abuse
              </div>
             </div>
            </span>
            <span aria-label="Page details" class="z80M1 FeRvI" jsaction="click:o6ZaF(preventDefault=true); mousedown:lAhnzb; mouseup:Osgxgf; mouseenter:SKyDAe; mouseleave:xq3APb;touchstart:jJiBRc; touchmove:kZeBdd; touchend:VfAz8(preventMouseEvents=true)" jsname="j7LFlb" jsslot="" role="menuitem" tabindex="-1">
             <div class="aBBjbd MbhUzd" jsname="ksKsZd">
             </div>
             <div class="uyYuVb oJeWuf" jsaction="JIbuQc:hriXLd;" jsname="Rg8K2c">
              <div class="jO7h3c">
               Page details
              </div>
             </div>
            </span>
           </div>
          </div>
         </div>
        </div>
       </div>
      </div>
      <div class="LqzjUe ynRLnc" data-last-updated-at-time="1636006694073" jsaction="focusin:gBxDVb(srlkmf); focusout:zvXhGb(srlkmf); click:ro2KTd(psdQ5e),Toy3n(V2zOu);JIbuQc:DSypkd(Bg3gkf);MxH79b:JdcaS;rcuQ6b:rcuQ6b;" jscontroller="j1RDQb">
       <div class="Q0cSn" jsname="psdQ5e">
       </div>
       <div class="hBW7Hb" jsname="bN97Pc">
        <div aria-disabled="false" aria-hidden="true" aria-label="Site actions" class="U26fgb mUbCce fKz7Od kpPxtd QMuaBc M9Bg4d" jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue; focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef;touchstart:p6p2H; touchmove:FwuNnf; touchend:yfqBxc(preventMouseEvents=true|preventDefault=true); touchcancel:JMtRjd;" jscontroller="VXdfxd" jsname="Bg3gkf" jsshadow="" role="button" tabindex="-1">
         <div class="VTBa7b MbhUzd" jsname="ksKsZd">
         </div>
         <span class="xjKiLb" jsslot="">
          <span class="Ce1Y1c" style="top: -12px">
           <svg class="NMm5M" focusable="false" height="24" viewbox="0 0 24 24" width="24">
            <path d="M11 17h2v-6h-2v6zm1-15C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zM11 9h2V7h-2v2z">
            </path>
           </svg>
          </span>
         </span>
        </div>
        <div class="hUphyc" jsname="srlkmf">
         <div class="YkaBSd">
          <div class="iBkmkf">
           <span>
            Page updated
           </span>
           <span class="dji00c" jsaction="AHmuwe:eGiyHb; mouseover:eGiyHb;" jsname="CFIm1b" role="contentinfo" tabindex="0">
           </span>
          </div>
         </div>
         <div class="YkaBSd" data-abuse-proto='%.@.null,null,"https://sites.google.com/gapp.nthu.edu.tw/lunarlander-ga",null,null,[],[]]' jsaction="click:dQ6O0c;" jscontroller="HYv29e">
          <div aria-disabled="false" aria-label="Report abuse" class="U26fgb kpPxtd J7BuEb" jsshadow="" role="button" tabindex="0">
           Report abuse
          </div>
         </div>
        </div>
       </div>
      </div>
     </div>
    </div>
    <script nonce="PlDSnyC9Wpbidv1t4uPZIw">
     DOCS_timing['cov']=new Date().getTime();
    </script>
    <script id="base-js" nonce="PlDSnyC9Wpbidv1t4uPZIw" src="https://www.gstatic.com/_/atari/_/js/k=atari.vw.en_US.x2vLtpY3xEU.O/d=1/rs=AGEqA5m196ioUWiwkoyCAkKZyrVEUO8edg/m=view">
    </script>
   </div>
  </div>
  <div jsaction="rcuQ6b:npT2md" jscontroller="YV8yqd">
   <div aria-atomic="true" aria-hidden="false" aria-live="assertive" aria-relevant="additions" class="IWfHH" id="docs-aria-speakable" role="region">
   </div>
  </div>
 </body>
</html>
