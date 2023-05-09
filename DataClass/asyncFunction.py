import asyncio 
import random
import time 

async def helloWorld():
    print('Hello World!')
    await asyncio.sleep(1)
    print()
    print('It wait 1 second for printing the next Hello world !')
    print()
    print('Hello World!')

async def addition(x,y):
    # wait = random.randint(0, 3)
    wait = 1
    await asyncio.sleep(wait)
    print(f'The addition of two number is {x+y}')
    print(f'It wait {wait} second for printing the output !')

async def substraction(x,y):
    # wait = random.randint(0, 3)
    wait = 2
    await asyncio.sleep(wait)
    print(f'The substratction of two number is {x-y}')
    print(f'It wait {wait} second for printing the output!')

async def multiply(x,y):
    # wait = random.randint(0, 3)
    wait = 3
    await asyncio.sleep(wait)
    print(f'The substratction of two number is {x*y}')
    print(f'It wait {wait} second for printing the output !')

    
async def main(x,y):
    await helloWorld()
    task1 = addition(x,y)
    task2 = substraction(x,y)
    task3 =  multiply(x,y)
    print(f"started at {time.strftime('%X')}") 
    await task1
    await task2
    await task3 
    print(f"started at {time.strftime('%X')}") 

if __name__ == '__main__':
    asyncio.run(main(10,3))
    
    
