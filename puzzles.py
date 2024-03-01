from random import randint, sample, sample, choice
import regex as re
from typing import Literal

ops = ["+","-","*","/"]

def randints(a: int,b: int,*,k=1,duplicates=False) -> list[int]:

    output = [randint(a,b) for _ in range(k)] if duplicates else sample(range(a, b + 1), k=k)
    return output

def check_one_operation(nums,target):
    for num1 in nums:
        for num2 in nums:
            for op in ops:
                if eval_nums(num1,num2,op) == target:
                    return True
    return False

def create_target(nums: list[int],min_range,max_range):
    target = -1
    counter = 0
    while (not min_range < target < max_range) or target in nums or check_one_operation(nums,target):
        if counter >= 50:
            return -2, "Error"
        self_ops = ops.copy()
        numbers = sample(nums,k=len(nums))
        total_steps = len(nums)-1
        target = numbers[0]
        solution = f"{target}"
        for idx, number in enumerate(numbers[1:total_steps+1]):
            operation = choice(self_ops)
            if operation == "*":
                self_ops.remove(operation)
            if idx == total_steps-1 and "*" in self_ops:
                operation = "*"
                self_ops.remove(operation)
            while operation == "/" and not (target/number).is_integer():
                operation = choice(self_ops)
            solution += f" {operation} {number}"
            target = eval_nums(target,number,operation)
        counter += 1
    return int(target), solution

def str_list(object=[]) -> list[str]:
    return [str(i) for i in object]

def eval_nums(num1,num2,op):
    if op == "+":
        return num1 + num2
    if op == "-":
        return num1 - num2
    if op == "*":
        return num1 * num2
    if op == "/":
        return num1 / num2
    if op == "%":
        return num1 % num2

def display_nums(nums,target):
    display = ""
    if len(nums) <= 1:
        display += f"Your numbers are {nums[0]}. "
    else:
        display += f"Your numbers are {", ".join(str_list(nums[:-1]))} and {nums[-1]}. "
    display += f"Your goal is {target}.\nYou can use + - * or / and may use each number at most once."
    return display

def create_puzzle(difficulty: Literal["easy","normal","hard"]):
    if difficulty == "easy":
        num_nums = 6
        min_range = 2
        max_range = 10
    if difficulty == "normal":
        num_nums = 5
        min_range = 5
        max_range = 20
    if difficulty == "hard":
        num_nums = 4
        min_range = 8
        max_range = 30
    solution = "Error"
    target = -1
    while solution == "Error" or target in (-1,-2):
        allowed_nums = sorted(randints(min_range,max_range,k=num_nums,duplicates=False))
        target, solution = create_target(allowed_nums,min_range=num_nums*4,max_range=num_nums*10)
    return display_nums(allowed_nums,target)