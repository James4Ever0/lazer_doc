<?php
/*sorry you fucking pussy cat.
 *this fucking platform does not suppory threaded php
 *fucking fucked php!
 * */
?>

these lines will simply be ignored.

with Threads, Workers and Threaded objects.

Warning: The pthreads extension cannot be used in a web server environment. Threading in PHP should therefore remain to CLI-based applications only.

Simple Test

#!/usr/bin/php
<?php
class AsyncOperation extends Thread {

    public function __construct($arg) {
        $this->arg = $arg;
    }

    public function run() {
        if ($this->arg) {
            $sleep = mt_rand(1, 10);
            printf('%s: %s  -start -sleeps %d' . "\n", date("g:i:sa"), $this->arg, $sleep);
            sleep($sleep);
            printf('%s: %s  -finish' . "\n", date("g:i:sa"), $this->arg);
        }
    }
}

// Create a array
$stack = array();

//Initiate Multiple Thread
foreach ( range("A", "D") as $i ) {
    $stack[] = new AsyncOperation($i);
}

// Start The Threads
foreach ( $stack as $t ) {
    $t->start();
}

?>
