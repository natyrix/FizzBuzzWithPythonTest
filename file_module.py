config = {
    3: 'Fizz',
    5:'Buzz',
    9:'Dong'
}

def fizzBuzz(numbers, config=config):
    val = ''
    for number in numbers:
        for key, value in config.items():
            if number%key == 0:
                val += value
        return val if val!='' else number


