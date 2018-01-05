#include "loops.f90"

program test
  implicit none
  integer :: i, j
  integer, dimension(:), allocatable :: indx1, indx2
  integer :: Ne, Nmod
  integer :: r1, r2 ! aux variables
  
  Ne = 4
  allocate(indx1(Ne))
  Nmod = 20
  indx1(:) = 1
 
  mps_FOR(i, 1, indx1, Ne, Nmod, r1, r2)
  
      print *, i, indx1
    
  END_mps_FOR(i)
  
end program test

