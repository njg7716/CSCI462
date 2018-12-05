#!/usr/bin/python3
import random
#This program was written by Nicholas Graca njg7716@rit.edu

#The goal of this program is to implement the Miller-Rabin
#primality test for odd integers between 95,000-105,000

#This function implements the Miller-Rabin primality test algorithm
def mil_rab_test(vals, minnum):
#Computes u and r because p'-1 = 2^(u)*r
        r = minnum - 1
        u = 0
        while u % 2 == 0:
                u = u + 1
                r = r// 2
        a = 2
#Instead of generating a random number s times, go through them all
        while a <=((minnum-1)):
                z = pow(a,r,minnum)
                if z == 1:
                        a = a + 1
                        vals.append(minnum)
                        continue #minnum might be prime
                i = 0
                for i in range(u-1):
                        if z == -1:
                                a = a +1
                                vals.append(minnum)
                                break#minnum might be prime
                        z = (z**2) % minnum
                a = a +1
        #If it gets through this loop then it is definetly composite

#This is the main function that stores the base and max values and runs through them all
def main():
        new = []
        m = {}
        probs = []
        minnum = 95000
        maxnum = 105000
        vals = []
#primes is a list of all prime numbers between 95000 and 105000
        primes = [95003,95009,95021,95027,95063,95071,95083,95087,95089,95093,95101,95107,95111,95131,95143,95153,95177,95189,95191,95203,95213,95219,95231,95233,95239,95257,95261,95267,95273,95279,95287,95311,95317,95327,95339,95369,95383,95393,95401,95413,95419,95429,95441,95443,95461,95467,95471,95479,95483,95507,95527,95531,95539,95549,95561,95569,95581,95597,95603,95617,95621,95629,95633,95651,95701,95707,95713,95717,95723,95731,95737,95747,95773,95783,95789,95791,95801,95803,95813,95819,95857,95869,95873,95881,95891,95911,95917,95923,95929,95947,95957,95959,95971,95987,95989,96001,96013,96017,96043,96053,96059,96079,96097,96137,96149,96157,96167,96179,96181,96199,96211,96221,96223,96233,96259,96263,96269,96281,96289,96293,96323,96329,96331,96337,96353,96377,96401,96419,96431,96443,96451,96457,96461,96469,96479,96487,96493,96497,96517,96527,96553,96557,96581,96587,96589,96601,96643,96661,96667,96671,96697,96703,96731,96737,96739,96749,96757,96763,96769,96779,96787,96797,96799,96821,96823,96827,96847,96851,96857,96893,96907,96911,96931,96953,96959,96973,96979,96989,96997,97001,97003,97007,97021,97039,97073,97081,97103,97117,97127,97151,97157,97159,97169,97171,97177,97187,97213,97231,97241,97259,97283,97301,97303,97327,97367,97369,97373,97379,97381,97387,97397,97423,97429,97441,97453,97459,97463,97499,97501,97511,97523,97547,97549,97553,97561,97571,97577,97579,97583,97607,97609,97613,97649,97651,97673,97687,97711,97729,97771,97777,97787,97789,97813,97829,97841,97843,97847,97849,97859,97861,97871,97879,97883,97919,97927,97931,97943,97961,97967,97973,97987,98009,98011,98017,98041,98047,98057,98081,98101,98123,98129,98143,98179,98207,98213,98221,98227,98251,98257,98269,98297,98299,98317,98321,98323,98327,98347,98369,98377,98387,98389,98407,98411,98419,98429,98443,98453,98459,98467,98473,98479,98491,98507,98519,98533,98543,98561,98563,98573,98597,98621,98627,98639,98641,98663,98669,98689,98711,98713,98717,98729,98731,98737,98773,98779,98801,98807,98809,98837,98849,98867,98869,98873,98887,98893,98897,98899,98909,98911,98927,98929,98939,98947,98953,98963,98981,98993,98999,99013,99017,99023,99041,99053,99079,99083,99089,99103,99109,99119,99131,99133,99137,99139,99149,99173,99181,99191,99223,99233,99241,99251,99257,99259,99277,99289,99317,99347,99349,99367,99371,99377,99391,99397,99401,99409,99431,99439,99469,99487,99497,99523,99527,99529,99551,99559,99563,99571,99577,99581,99607,99611,99623,99643,99661,99667,99679,99689,99707,99709,99713,99719,99721,99733,99761,99767,99787,99793,99809,99817,99823,99829,99833,99839,99859,99871,99877,99881,99901,99907,99923,99929,99961,99971,99989,99991,100003,100019,100043,100049,100057,100069,100103,100109,100129,100151,100153,100169,100183,100189,100193,100207,100213,100237,100267,100271,100279,100291,100297,100313,100333,100343,100357,100361,100363,100379,100391,100393,100403,100411,100417,100447,100459,100469,100483,100493,100501,100511,100517,100519,100523,100537,100547,100549,100559,100591,100609,100613,100621,100649,100669,100673,100693,100699,100703,100733,100741,100747,100769,100787,100799,100801,100811,100823,100829,100847,100853,100907,100913,100927,100931,100937,100943,100957,100981,100987,100999,101009,101021,101027,101051,101063,101081,101089,101107,101111,101113,101117,101119,101141,101149,101159,101161,101173,101183,101197,101203,101207,101209,101221,101267,101273,101279,101281,101287,101293,101323,101333,101341,101347,101359,101363,101377,101383,101399,101411,101419,101429,101449,101467,101477,101483,101489,101501,101503,101513,101527,101531,101533,101537,101561,101573,101581,101599,101603,101611,101627,101641,101653,101663,101681,101693,101701,101719,101723,101737,101741,101747,101749,101771,101789,101797,101807,101833,101837,101839,101863,101869,101873,101879,101891,101917,101921,101929,101939,101957,101963,101977,101987,101999,102001,102013,102019,102023,102031,102043,102059,102061,102071,102077,102079,102101,102103,102107,102121,102139,102149,102161,102181,102191,102197,102199,102203,102217,102229,102233,102241,102251,102253,102259,102293,102299,102301,102317,102329,102337,102359,102367,102397,102407,102409,102433,102437,102451,102461,102481,102497,102499,102503,102523,102533,102539,102547,102551,102559,102563,102587,102593,102607,102611,102643,102647,102653,102667,102673,102677,102679,102701,102761,102763,102769,102793,102797,102811,102829,102841,102859,102871,102877,102881,102911,102913,102929,102931,102953,102967,102983,103001,103007,103043,103049,103067,103069,103079,103087,103091,103093,103099,103123,103141,103171,103177,103183,103217,103231,103237,103289,103291,103307,103319,103333,103349,103357,103387,103391,103393,103399,103409,103421,103423,103451,103457,103471,103483,103511,103529,103549,103553,103561,103567,103573,103577,103583,103591,103613,103619,103643,103651,103657,103669,103681,103687,103699,103703,103723,103769,103787,103801,103811,103813,103837,103841,103843,103867,103889,103903,103913,103919,103951,103963,103967,103969,103979,103981,103991,103993,103997,104003,104009,104021,104033,104047,104053,104059,104087,104089,104107,104113,104119,104123,104147,104149,104161,104173,104179,104183,104207,104231,104233,104239,104243,104281,104287,104297,104309,104311,104323,104327,104347,104369,104381,104383,104393,104399,104417,104459,104471,104473,104479,104491,104513,104527,104537,104543,104549,104551,104561,104579,104593,104597,104623,104639,104651,104659,104677,104681,104683,104693,104701,104707,104711,104717,104723,104729,104743,104759,104761,104773,104779,104789,104801,104803,104827,104831,104849,104851,104869,104879,104891,104911,104917,104933,104947,104953,104959,104971,104987,104999]
        while minnum <= maxnum:
                t = len(vals)
                new = []
                if minnum % 2 == 0:
                        minnum = minnum + 1
                        continue
                mil_rab_test(new, minnum)
                vals= vals + new
                if len(new) == 0: #Checks if the number is possibly prime
                        minnum = minnum + 1
                        continue
#The next loop will check to see if the number is a liar and if it is it will then run the test again to see how many
#times a false positive occurs and then print out the probability.
                if minnum in primes:#Checks if the number is prime
                        minnum = minnum + 1
                        continue
                x = len(new)
                tot = minnum-1
                m[(x/tot)] = minnum#maps the number to the probability
                probs.append((x/tot))#computes probability and adds it to the list
                #Uncomment next line to print out all the liars and probabilities
#                print(str(minnum) + " is a liar! The percentage that it is wrong is "+str(round(x/tot, 3)))
                minnum = minnum + 1
        #This part will print out the top ten probabilities and their number.
        probs.sort()
        print("The top ten probabilities with its corresponding numbers are:")
        i = -1
        y = 0
        while y < 10:
                print(str(round(probs[i], 3)) + ": " + str(m[probs[i]]))
                i = i - 1
                y = y + 1
main()

''' The following is the output of this program. It takes a long time to run.
The top ten probabilities with its corresponding numbers are:
97921: 0.33087214052287583
96049: 0.19826545060802933
101101: 0.1780316518298714
104653: 0.12417345105683598
96641: 0.0662148178807947
102173: 0.06580080648318522
95161: 0.06304119377889869
101661: 0.061528624827857564
104833: 0.058026175213675216
97681: 0.05404381654381654
'''
