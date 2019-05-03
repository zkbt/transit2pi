import transit2pi as t2p

'''
Here is the script that will help us test 3 cases in the Fiske Planetarium.
'''
#Case 1: rs = 1 Rsun, rp=0.10049, a=0.0465*212
t2p.make_transit_curve(a=0.0465*212,rp=0.10049,filename='Transit_Jupiter_like_1.png')
#Case 2: rs = 1Rsun, rp=0.03654, a=0.0465*212
t2p.make_transit_curve(a=0.0465*212,rp=0.03654,filename='Transit_Neptune_like_1.png')
#Case 3: rs = 0.2Rsun, rp=5, a=0.0465*212
t2p.make_transit_curve(a=0.0465*212,rp=5*0.03654,filename='Transit_Neptune_like_2.png')
