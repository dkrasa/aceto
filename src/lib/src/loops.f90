#define mps_FOR( ii, Nst, indx, Nex, Nmod, r1, r2) \
ii=Nst;\
r1=1;\
indx(r1)=indx(r1)-1;\
do;\
indx(r1)=indx(r1)+1;\
if(indx(r1)>Nmod)then;\
r1=r1+1;\
if(r1==(Nex+1))exit;\
indx(r1-1)=indx(r1)+1;\
do r2=1,r1-2;\
indx(r2)=indx(r1-1);\
enddo;\
else;\
r1=1

#define END_mps_FOR(ii) \
    ii = ii + 1; \
  end if; \
end do


