```c
/* single word (4) or double word (8) alignment */
 #define ALIGNMENT 8 
/* rounds up to the nearest multiple of ALIGNMENT */
 #define ALIGN(size) (((size) + (ALIGNMENT-1)) & ~0x7)
 
 
 #define INITCHUNKSIZE (1<<6)
 
#define LISTLIMIT     20      
#define REALLOC_BUFFER  (1<<7)  
 
```

