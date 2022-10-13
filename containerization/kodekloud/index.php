<?php

class Task
{
    /**
     * 
     * @var mixed
     */
    public $data;

    /**
     * 
     * @var string
     */
    public $type;

    public function __construct(string $type, $data = null)
    {
        $this->type = $type;
        $this->data = $data;
    }
}

class PoolExecutor
{

    /**
     * 
     * @var callable
     */
    private $processor;

    public function __construct(callable $processor)
    {
        $this->processor = $processor;
    }

    public function call(Task $command)
    {
        ($this->processor)($command);
    }
}

function createPool(callable $handler, int $size = 1)
{
    $executor = new PoolExecutor($handler);
    $buffer = [];
    $fn = function ($values) use ($executor) {
        foreach ($values as $value) {
            $executor->call($value);
        }
    };
    while (true) {
        $task = yield;
        if (!($task instanceof Task)) {
            $type = (is_object($task) ? get_class($task) : gettype($task));
            throw new Exception('Invalid task object, require instance of ' . Task::class . ', ' . $type . ' given');
        }
        if (strtolower($task->type) === 'quit') {
            if (!empty($buffer)) {
                $fn($buffer);
                $buffer = [];
            }
            printf("Completing Job....\n");
            break;
        }
        $buffer[] = $task;
        if ($size === count($buffer)) {
            $fn($buffer);
            $buffer = [];
        }
    }
}


$pool = createPool(
    function (Task $task) {
        printf("Processing: %s\n", $task->type);
        printf("Data: %d\n", $task->data);
    },
    2
);

$i = 0;
while ($pool->valid()) {
    if ($i == 10) {
        $pool->send(new Task('quit'));
        continue;
    }
    $i++;
    sleep(1);
    $pool->send(new Task('Task' . $i, $i));
}
printf('Program completes...!');