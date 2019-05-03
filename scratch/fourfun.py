#import simulatedmovie as sm
#import keplermovie as km
import subprocess

#This works!! so far for simulated data. Next is to animate m2t
# and create same functions


x =input("Enter yes for bouncing ball or no for not")
def Sim(x="yes"):
    if x =="yes":
        subprocess.call(["python", "kepmovie.py"])
    else:
        subprocess.call(["python", "simulatedmovie.py"])

def Kepler(x='yes'):
    if x =='yes':
        subprocess.call(['python', 'keplermovie.py'])
    else:
        subprocess.call(['python', 'make2pitransit_2.py'])


#x =raw_input("Enter yes for bouncing ball or no for not")

#plot a simulated plot

#or plot a simulated a plot with ball

#if user typed ball then plot with ball
#if user

#if user types in function period, to, blah batman params,
#then

#if condition:
#    import fileA as file
#else:
#    import fileB as file
#file.foo()
#if ball =  'No'
#import simulatedmovie as sm
#import kepmovie as km


#ball = input('')
#def simulated_transit2pi(x='yes'):
  #if x == 'yes':
      #import kepmovie as km
  #elif x == 'no':
      #import simulatedmovie as sm
#.foo()
