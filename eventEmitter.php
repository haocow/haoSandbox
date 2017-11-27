<?php

/**
 * Pub/Sub Challenge
 *
 * FIRST: COPY/PASTE ALL THE CODE IN THE TEXTFIELD BELOW AND EDIT IT THERE
 *
 * 1. The goal is to build a very simple PubSub/event class in PHP.
 *    We will create an EventEmitter object and then we'll subscribe to events and trigger them.
 *    Subscribing to an event simply adds a callback to be run when the event is triggered.
 *    Triggering an event (emit) should run all the attached callbacks.
 * 2. Don't overthink it. The solution should only take a few minutes and a few lines of code.
 *    Build only what you need to get the desired ouput.
 *
 * Constraints:
 * 1. Although we only use error/success events, please build the class to handle arbitrary events.
 * 2. Events data will always be an associative array.
 * 3. A callback should always be safe to call.
 */

class EventEmitter {

    private $callbacks;

    public function __construct() {
        $this->callbacks = array();
    }

    public function emit($event, $context) {
        if (!isset($this->callbacks[$event])) {
            return;
        } else {
            foreach ($this->callbacks[$event] as $callback) {
                $callback($context);
            }
        }
    }

    public function subscribe($event, $callback) {
        if (!isset($this->callbacks[$event])) {
            $this->callbacks[$event] = array($callback);
        } else {
            $this->callbacks[$event][] = $callback;
        }
    }

}

$emitter = new EventEmitter;

$error_callback = function($data) {
    echo "Error 1. {$data["message"]} \n";
};

$error_callback2 = function($data) {
    echo "Error 2. {$data["message"]} \n";
};

$success_callback = function($data) {
    echo "SUCCESS! {$data["message"]} \n";
};

$emitter->emit("error", ["message" => "Error one."]);

$emitter->subscribe("error", $error_callback);
$emitter->emit("error", ["message" => "Second error."]);

$emitter->subscribe("error", $error_callback2);
$emitter->emit("error", ["message" => "Yet another error."]);

$emitter->subscribe("success", $success_callback);
$emitter->emit("success", ["message" => "Great success!."]);

// Expected output:

// Error 1. Second error.
// Error 1. Yet another error.
// Error 2. Yet another error.
// SUCCESS! Great success!