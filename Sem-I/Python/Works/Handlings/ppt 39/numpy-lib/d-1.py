
import  numpy  as  np
'''
#Creating Arrays with Specific Datatypes
print('Creating Arrays with Specific Datatypes:')
arr  =  np. array ([1 ,  2 ,  3],  dtype =np. int32 )
print(arr)

#conversion of datatype
print('Datatype Conversion:')
arr  =  arr. astype ( np. float64 )
print(arr,' after conversion to float64\n')

#Vectorized Operations
print('Vectorized Operations:')
arr1  =  np. array ([4 ,  5 ,  6])
sum_arr  =  arr  +  arr1
print (sum_arr,' after addition')
#auto conversion to higher datatype
print (sum_arr.dtype ,' datatype after addition')
sub_arr  =  arr1  -  arr
print (sub_arr,' after subtraction')
mul_arr  =  arr  *  arr1
print (mul_arr,' after multiplication')
div_arr  =  arr1  /  arr
print (div_arr,' after division\n')

#universal Functions 
#ufuncs
print('Universal Functions:')
arr  =  np. array ([1 ,  4 ,  9])
sqrt_arr  =  np.sqrt( arr)
print (sqrt_arr,' after square root')
exp_arr  =  np.exp( arr)
print (exp_arr,' after exponentiation')
log_arr  =  np.log( arr)
print (log_arr,' after natural logarithm')
sin_arr  =  np.sin( arr)
print (sin_arr,' after sine function')
cos_arr  =  np.cos( arr)
print (cos_arr,' after cosine function')
tan_arr  =  np.tan( arr)
print (tan_arr,' after tangent function\n')
#returns always float64 for precision as in python documentation.
#python float type is equivalent to numpy float64 type and double-precision (64-bit).

#aggregate Functions
print('Aggregate Functions:')
arr  =  np. array ([1 ,  2 ,  3 ,  4 ,  5])
sum_val  =  np.sum( arr)
print (sum_val,' sum of array elements')
mean_val  =  np.mean( arr)
print (mean_val,' mean of array elements')
max_val  =  np.max( arr)
print (max_val,' maximum of array elements')
min_val  =  np.min( arr)
print (min_val,' minimum of array elements')
std_val  =  np.std( arr)
print (std_val,' standard deviation of array elements')
var_val  =  np.var( arr)
print (var_val,' variance of array elements')
median_val  =  np.median( arr)
print (median_val,' median of array elements')
percentile_val  =  np.percentile( arr,  50)
print (percentile_val,' 50th percentile of array elements\n')

#slicing and Indexing
print('Slicing and Indexing:')
arr  =  np. array ([1 ,  2 ,  3 ,  4 ,  5])
slice_arr  =  arr [1:4:1]  #slicing from index 1 to 3
print (slice_arr,' sliced array from index 1 to 3')

#array reshaping
print('Array Reshaping:')
arr  =  np. array ([[1 ,  2 ,  3],  [4 ,  5 ,  6]])
print (arr,' original array')
reshaped_arr =  arr. reshape ((3 ,  2))
print (reshaped_arr,' reshaped array to 3x2')

#broadcasting
print('Broadcasting:')
arr1  =  np. array ([1 ,  2 ,  3])
arr2  =  np. array ([[1] ,  [2],  [3]])
broadcast_sum  = arr1  +  arr2
print (broadcast_sum,' after broadcasting addition\n')
#Note: Broadcasting allows numpy to perform operations on arrays of different shapes.
#It automatically expands the smaller array to match the shape of the larger array during arithmetic operations.
#This leads to efficient memory usage and faster computations.
#Reference: https://numpy.org/doc/stable/user/quickstart.html#universal-functions-ufuncs
#Broadcasting allows NumPy to perform element-wise operations on arrays of different shapes.
#The smaller array is "broadcast" across the larger array so that they have compatible shapes.
#This is particularly useful for performing operations without the need for explicit replication of data, leading to more efficient memory usage and faster computations.

#boolean Indexing
print('Boolean Indexing:')
arr  =  np. array ([1 ,  2 ,  3 ,  4 ,  5])
bool_idx  =  arr  >  3
filtered_arr  =  arr[ bool_idx]
print (filtered_arr,' filtered array with elements greater than 3\n')
#or directly
#filtered_arr  =  arr[ arr  >  3]

#sorting
print('Sorting:')
arr  =  np. array ([3 ,  1 ,  2])
sorted_arr  =  np. sort( arr)	#  array ([1 ,  2 ,  3]) 
arr. sort ()
print(arr,' sorted array using method')
print (sorted_arr,' sorted array using fucntion \n')

#linear Algebra Operations
print('Linear Algebra Operations:')
mat1  =  np. array ([[1 ,  2],  [3 ,  4]])
mat2  =  np. array ([[5 ,  6],  [7 ,  8]])
mat_mult  =  np. dot ( mat1 ,  mat2)
print (mat_mult,' after matrix multiplication') 
mat_mult_inv  =  np.matmul ( mat1 ,  mat2)
print (mat_mult_inv,' after multiplying matrix using .matmul')
mat_inv  =  np. linalg .inv ( mat1)
print (mat_inv,' after matrix inversion')
mat_transpose  =  np. transpose ( mat1)
print (mat_transpose,' after matrix transposition')
mat_det  =  np. linalg .det ( mat1)
print (mat_det,' after calculating determinant\n')

#static functions
print('Statistical Functions:')
arr  =  np. array ([1 ,  2 ,  3 ,  4 ,  5])
mean_val  =  np. mean ( arr)
print (mean_val,' mean of array elements using static function')
median_val  =  np. median ( arr)
print (median_val,' median of array elements using static function')

#Descriptive Statistics
print('Descriptive Statistics:')
arr  =  np. array ([1 ,  2 ,  3 ,  4 ,  5])
std_val  =  np. std ( arr)
print (std_val,' standard deviation of array elements using static function')
var_val  =  np. var ( arr)
print (var_val,' variance of array elements using static function\n')

#Percentiles and Quartiles
print('Percentiles and Quartiles:')
arr  =  np. array ([1 ,  2 ,  3 ,  4 ,  5])
percentile_50  =  np. percentile ( arr , 0.1)	
quantile_25  =  np. quantile ( arr ,  0.25)
print (percentile_50,' 0.1th percentile using static function')
print (quantile_25,' 25th quantile using static function')	

#min max range
print('Min, Max, and Range:')
arr  =  np. array ([1 ,  2 ,  3 ,  4 ,  5])
min_val  =  np. min ( arr)
print (min_val,' minimum of array elements using static function')
max_val  =  np. max ( arr)
print (max_val,' maximum of array elements using static function')
range_val  =  np. ptp ( arr)
print (range_val,' range of array elements using static function\n')
#ptp: Peak to Peak (Range) = max - min

#sum product and cumulative operations functions
print('Sum, Product, and Cumulative operations Functions:')
arr  =  np. array ([1 ,  2 ,  3 ,  4 ,  5])
sum_val  =  np. sum( arr)
print (sum_val,' sum of array elements using static function')
product_val  =  np. prod ( arr)
print (product_val,' product of array elements using static function')
cumsum_val  =  np. cumsum ( arr)
print (cumsum_val,' cumulative sum of array elements using static function')
cumsum_val  =  np. cumprod ( arr)
print (cumsum_val,' cumulative product of array elements using static function\n')
#cumsum: Cumulative Sum
#prod: Product of array elements

#correlation and covariance
print('Correlation and Covariance:')
arr1  =  np. array ([1 ,  2 ,  3 ])
arr2  =  np. array ([4 , 5 ,  6 ])
correlation_val  =  np. corrcoef ( arr1 ,  arr2)
print (correlation_val,' correlation coefficient between two arrays using static function')
covariance_val  =  np. cov ( arr1 ,  arr2)
print (covariance_val,' covariance between two arrays using static function\n')
#corrcoef: Correlation Coefficient
#cov: Covariance

#fin

#id to 2d addition that is broadcasting
arr2d=np.array([[1,2,3],[4,5,6]])
arr1d=np.array([1,2,3])
result=arr2d+arr1d
print(result)

#axis in mean concept
data=np.array([[1,2,3],[4,5,6],[7,8,9]])
mean=np.mean(data, axis=1)
centered_data=data-mean
print("Mean:", centered_data)

#boolean amsking
data=np.array([10,20,30,40,50])
mask=data>20
print(data[mask])


#logical operators
print('Logical Operators:')
#and &
#or |
#not ~
'''


