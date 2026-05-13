{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "eaf19799-9db8-4baa-92ce-2e5df9a87689",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15\n"
     ]
    }
   ],
   "source": [
    "def calculate_area(length,width):\n",
    "    area = length*width\n",
    "    return area\n",
    "\n",
    "result= calculate_area(5, 3)\n",
    "print (result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "de196ded-af06-4ec1-a8ec-6215325446e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def greet(name):\n",
    "    print(\"Salve,\" + name + \"!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "0bbcb127-8f97-46c7-924d-0d4dc7825b70",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Salve, Maira !\n"
     ]
    }
   ],
   "source": [
    "greet(\" Maira \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "a7439ad2-fe99-4c2d-b5d6-80a8644857f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import datetime\n",
    "\n",
    "def greet_with_time(name):\n",
    "    current_time = datetime.now().strftime(\" %H:%M:%S\")\n",
    "    print(f\"Hello, {name}! The current time is {current_time}.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "7bda5874-fedd-469b-a6df-f3932d242f4b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, Maira! The current time is  15:57:52.\n"
     ]
    }
   ],
   "source": [
    "greet_with_time(\"Maira\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "54c3adea-a4fa-4c4a-b9ca-dea096102a6c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_average(num1, num2, num3):\n",
    "    average = (num1 + num2 + num3) / 3\n",
    "    return average"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "a067d152-0b39-4482-9265-920cbd9039f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average: 20.0\n"
     ]
    }
   ],
   "source": [
    "result = calculate_average(10, 20, 30)\n",
    "print(\"Average:\", result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "59b5f017-793b-493b-86ad-9a04ba64a19a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "90.0\n",
      "80.0\n"
     ]
    }
   ],
   "source": [
    "def calculate_discount(price, discount_percentage=10):\n",
    "    discount_amount = (price * discount_percentage) / 100\n",
    "    final_price = price - discount_amount\n",
    "    return final_price\n",
    "\n",
    "print(calculate_discount(100))      \n",
    "print(calculate_discount(100, 20))  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "ff249e4d-5abf-4e38-bef2-303c45bdf977",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name: Sara\n",
      "Age: 25\n",
      "City: Lahore\n"
     ]
    }
   ],
   "source": [
    "def print_info(name, age, city):\n",
    "    print(f\"Name: {name}\")\n",
    "    print(f\"Age: {age}\")\n",
    "    print(f\"City: {city}\")\n",
    "\n",
    "\n",
    "print_info(name=\"Sara\", age=25, city=\"Lahore\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "103d0652-f0ad-4517-a7b4-5978681991e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n",
      "30\n"
     ]
    }
   ],
   "source": [
    "def find_max(*args):\n",
    "    return max(args)\n",
    "print(find_max(3, 7, 2, 9, 5))   \n",
    "print(find_max(10, 20, 30))      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "c4f4132a-fd99-40df-b187-badff97104ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Factorial of 5 is 120\n"
     ]
    }
   ],
   "source": [
    "def factorial(n):\n",
    "    if n == 0 or n == 1:\n",
    "        return 1\n",
    "    \n",
    "    return n * factorial(n - 1)\n",
    "\n",
    "num = 5\n",
    "print(\"Factorial of\", num, \"is\", factorial(num))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "96f36560-dced-4552-bd37-d712a36c61cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 9, 16, 25]\n",
      "[1, 4, 9, 16, 25]\n"
     ]
    }
   ],
   "source": [
    "def apply_function(func, numbers):\n",
    "    result = []\n",
    "    \n",
    "    for num in numbers:\n",
    "        result.append(func(num))\n",
    "    \n",
    "    return result\n",
    "\n",
    "def square(x):\n",
    "    return x * x\n",
    "\n",
    "def double(x):\n",
    "    return x * x\n",
    "numbers = [1, 2, 3, 4, 5]\n",
    "\n",
    "print(apply_function(square, numbers))\n",
    "print(apply_function(double, numbers))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
