<?php

if (count($argv) != 4) {
    print "WRONG NUMBER OF ARGUMENTS PROVIDED\n";
    return;
}

$sizeA = min($argv[1], $argv[2]);
$sizeB = max($argv[1], $argv[2]);
$target = $argv[3];
print "**Starting for params bucketA size = $sizeA, bucketB size = $sizeB, target = $target**\n";
$steps = buckets($sizeA, $sizeB, $target);
if ($steps != -1) {
    Bucket::printSteps($steps);
}
print "\n";

class Bucket
{
    /**
     * @var int $size
     */
    private $size;

    /**
     * @var int $filled
     */
    private $filled;

    public function __construct($size)
    {
        $this->size = $size;
        $this->filled = 0;
    }

    /**
     * transfers max possible of bucketA into bucketB
     *
     * @param Bucket $bucketA
     * @param Bucket $bucketB
     */
    static public function transfer($bucketA, $bucketB)
    {
        $transferAmount = min($bucketA->getFilled(), $bucketB->getUnfilled());
        $bucketA->setFilled($bucketA->getFilled() - $transferAmount);
        $bucketB->setFilled($bucketB->getFilled() + $transferAmount);
    }

    /**
     * helper function to help print out buckets for debug
     *
     * @param array $steps
     */
    static public function printSteps($steps)
    {
        $fullSteps = "";
        foreach ($steps as $step) {
            $fullSteps .= "(" . $step[0] . ", " . $step[1] . ")->";
        }
        $fullSteps .= "DONE";

        print $fullSteps;
    }

    /**
     * returns if bucket is full
     *
     * @return bool
     */
    public function isFull()
    {
        return ($this->filled == $this->size);
    }

    /**
     * returns if bucket is empty
     *
     * @return bool
     */
    public function isEmpty()
    {
        return ($this->filled == 0);
    }

    /**
     * sets bucket to full
     */
    public function fill()
    {
        $this->filled = $this->size;
    }

    /**
     * sets bucket to empty
     */
    public function dump()
    {
        $this->filled = 0;
    }

    private function getUnfilled()
    {
        return $this->size - $this->filled;
    }

    private function setFilled($newFilled)
    {
        $this->filled = $newFilled;
    }

    public function getFilled()
    {
        return $this->filled;
    }
}

/**
 * @param int $sizeA
 * @param int $sizeB
 * @param int $target
 *
 * @return array|int
 */
function buckets($sizeA, $sizeB, $target)
{
    $bucketA = new Bucket($sizeA);
    $bucketB = new Bucket($sizeB);

    // Special case if target is exactly the combination of the bucket sizes
    if ($sizeA + $sizeB == $target) {
        return [
            [0,0],
            [$sizeA,0],
            [$sizeA, $sizeB],
        ];
    }

    // Special cases if target is impossible given the bucket sizes OR
    // if target is greater than both bucket sizes combined
    if ($target % gcd($sizeA, $sizeB) != 0 ||
        $target > $sizeA + $sizeB) {
        print "FINDING SOLUTION IMPOSSIBLE\n";
        return -1;
    };

    $aToB = pourLoop(clone $bucketA, clone $bucketB, $target);
    $bToA = pourLoop(clone $bucketB, clone $bucketA, $target);

    return (count($aToB) < count($bToA)) ? $aToB : $bToA;
}

/**
 * @param Bucket $bucketA
 * @param Bucket $bucketB
 * @param int    $target
 *
 * @return array|boolean
 */
function pourLoop($bucketA, $bucketB, $target)
{
    $steps = [[0,0]];
    while ($bucketA->getFilled() != $target &&
           $bucketB->getFilled() != $target &&
           ($bucketA->getFilled() + $bucketB->getFilled()) != $target) {
        if ($bucketA->isEmpty()) {
            $bucketA->fill();
        } elseif ($bucketB->isFull()) {
            $bucketB->dump();
        } else {
            Bucket::transfer($bucketA, $bucketB);
        }

        $steps[] = [$bucketA->getFilled(), $bucketB->getFilled()];
    }

    return $steps;
}

/**
 * returns the greatest common divisor (needed to figure out if the bucket sizes make this problem impossible)
 * @param int $a
 * @param int $b
 *
 * @return int
 */
function gcd($a, $b)
{
    if ($b == 0) {
        return $a;
    }

    return gcd($b, $a % $b);
}