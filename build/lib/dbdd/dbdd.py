number = 0

def add_one(number):
    return number + 1

width = os.get_terminal_size().columns

scriptsList = []
printSpaces = ""

def getCurrentTime():
    return datetime.datetime.utcnow().strftime("%H:%M:%S")
def print_important(message):
    print(f"{printSpaces}{Fore.BLUE}[{getCurrentTime()}] {Fore.WHITE}[IMPORTANT] {Fore.GREEN}{message}".center(width))    
def print_info(message):
    print(f"{printSpaces}{Fore.BLUE}[{getCurrentTime()}] {Fore.WHITE}[INFORMATION] {Fore.GREEN}{message}".center(width))
def print_cmd(command):
    print(f"{printSpaces}{Fore.BLUE}[{getCurrentTime()}] {Fore.WHITE}[COMMAND] {Fore.GREEN}{command}".center(width))
def print_sharecmd(author, command):
    print(f"{printSpaces}{Fore.BLUE}[{getCurrentTime()}] {Fore.WHITE}[SHARE COMMAND] {Fore.GREEN}({author}) {command}".center(width))
def print_error(error):
    print(f"{printSpaces}{Fore.BLUE}[{getCurrentTime()}] {Fore.WHITE}[ERROR] {Fore.GREEN}{error}".center(width))
def print_problem(message):
    print(f"{printSpaces}{Fore.BLUE}[{getCurrentTime()}] {Fore.WHITE}[PROBLEM] {Fore.GREEN}{message}".center(width))
def print_dbdd(message):
    print(f"{printSpaces}{Fore.BLUE}[{getCurrentTime()}] {Fore.WHITE}[DBDD] {Fore.GREEN}{message}".center(width))
def print_dbdd_info(firstmessage, secondmessage):
    spaces = ""
def input_info(message):
    input(f"{printSpaces}{Fore.BLUE}[{getCurrentTime()}] {Fore.WHITE}[INPUT] {Fore.GREEN}{message}: \n".center(width))

def include(filename):
        global scriptsList
        if os.path.exists(filename):
            scriptsList.append(filename)
            exec(codecs.open(filename, encoding="utf-8").read(), globals(), locals())

def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

@client.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        await ctx.send('[ERROR]: You\'re missing permission to execute this command', delete_after=3)
        print_error("You\'re missing permission to execute this command")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"[ERROR]: Missing arguments: {error}", delete_after=3)
        print_error(f"Missing arguments: {error}")
    elif isinstance(error, numpy.AxisError):
        await ctx.send('[ERROR] Invalid Image', delete_after=3)
        print_error("Invalid Image")
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send(f"[ERROR]: 404 Forbidden Access: {error}", delete_after=3)
        print_error(f"404 Forbidden Access: {error}")
    elif "Cannot send an empty message" in error_str:
        await ctx.send('[ERROR]: Message contents cannot be null', delete_after=3)
        print_error("Cannot send an empty message")
    else:
        await ctx.send(f'[ERROR]: {error_str}', delete_after=3)
        print_error(f"{error_str}")