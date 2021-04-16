program matmulf 

	implicit none
	character*100 :: ind
	character :: modo
	integer :: indint
	real*8, dimension (:,:), allocatable :: mat
	real*8, dimension (:), allocatable :: veten	  
	real*8, dimension (:), allocatable :: vetsa
	real :: start, finish
	integer i,j	
	
	call get_command_argument(1, ind)
	call get_command_argument(2, modo)
	read(ind, *) indint
	allocate (mat(indint,indint))
	allocate (veten(indint))
	allocate (vetsa(indint))
	call RANDOM_NUMBER(mat)
	call RANDOM_NUMBER(veten)
	vetsa = 0
	
	IF (modo == '0') THEN
		call CPU_TIME(start) 
		do i=1, indint
			do j=1, indint
				vetsa(i)=vetsa(i)+veten(j)*mat(i,j)		
			end do
		end do
		call CPU_TIME(finish)
	end if

	IF (modo == '1') THEN
		call CPU_TIME(start)
                do j=1, indint
                        do i=1, indint
                                vetsa(i)=vetsa(i)+veten(j)*mat(i,j)
                        end do
                end do
		call CPU_TIME(finish)
        end if


print *, INDINT, ":", finish-start








!	do i=1, indint
!		print *, "-----------------------------"
!		do j=1, indint
!			print *, mat(i,j)
!		end do
!	end do
!
!print *, "v1-----------------------------"
!do i=1, indint
!                print *, veten(i)
!        end do
!print *, "v2-----------------------------"
!do i=1, indint
!                print *, vetsa(i)
!        end do
!
!

end program matmulf
