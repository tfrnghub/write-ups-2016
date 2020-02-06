#python3
#sudo apt-get install libmpfr-dev libmpc-dev 
#pip install gmpy2
import sys
import libnum
from gmpy2 import *


    



if __name__ == "__main__":
    #p*q
    n1=19402643768027967294480695361037227649637514561280461352708420192197328993512710852087871986349184383442031544945263966477446685587168025154775060178782897097993949800845903218890975275725416699258462920097986424936088541112790958875211336188249107280753661467619511079649070248659536282267267928669265252935184448638997877593781930103866416949585686541509642494048554242004100863315220430074997145531929128200885758274037875349539018669336263469803277281048657198114844413236754680549874472753528866434686048799833381542018876362229842605213500869709361657000044182573308825550237999139442040422107931857506897810951
    #(p+2)*(q+2)
    n2=19402643768027967294480695361037227649637514561280461352708420192197328993512710852087871986349184383442031544945263966477446685587168025154775060178782897097993949800845903218890975275725416699258462920097986424936088541112790958875211336188249107280753661467619511079649070248659536282267267928669265252935757418867172314593546678104100129027339256068940987412816779744339994971665109555680401467324487397541852486805770300895063315083965445098467966738905392320963293379345531703349669197397492241574949069875012089172754014231783160960425531160246267389657034543342990940680603153790486530477470655757947009682859

    x=2
    #p+q
    s=(n2-n1-4)//x
    xx=s*s-4*n1
    delta,re=iroot(xx, 2)
    if re==False:
        print("iroot error")
        sys.exit(0)
    print(delta)
    p=s//2-delta//2
    q=s//2+delta//2
    print(p*q-n1)


    e=65537
    
    
    n=(p+2)*(q+2)
    fn=(p+1)*(q+1)
    d=invert(e,fn)
    



    enc=7991219189591014572196623817385737879027208108469800802629706564258508626010674513875496029177290575819650366802730803283761137036255380767766538866086463895539973594615882321974738140931689333873106124459849322556754579010062541988138211176574621668101228531769828358289973150393343109948611583609219420213530834364837438730411379305046156670015024547263019932288989808228091601206948741304222197779808592738075111024678982273856922586615415238555211148847427589678238745186253649783665607928382002868111278077054871294837923189536714235044041993541158402943372188779797996711792610439969105993917373651847337638929

    
    yy=pow(enc,d,n)

    
    e=65537
    n=p*q
    fn=(p-1)*(q-1)
    d=invert(e,fn)
    
    zz=pow(yy,d,n)
    '''
    while True:
        try:
            print(libnum.n2s(zz))
            break
        except:
            zz=zz//0x100
    '''
    zz=digits(zz,16)
    #zz=int(zz,16)
    print(zz)
    
    print(bytes.fromhex(zz))

    
    
