import asyncio
import os


async def change_files(x):
    files = os.listdir("f://test")

    for file in files:
        portion = os.path.splitext(file)
        print(portion)

        if portion[1] == '.py':
            newname = portion[0] + ".txt"
            os.chdir("f://test")
            os.rename(file, newname)

    return '{}任务完成'.format(x)


def callback(future):
    print("Callback:", future.result())


coroutine = change_files("修改扩展名")
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
loop.run_until_complete(task)
