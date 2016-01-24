<?php
/**
 * xxxx
 *
 * @author     lixiaohong <lixiaohong0212@gmail.com>
 */


/**
 * xxxx
 *
 * @author     lixiaohong <lixiaohong0212@gmail.com>
 */



require_once __DIR__.'/lib/php/lib/Thrift/ClassLoader/ThriftClassLoader.php';

use Thrift\ClassLoader\ThriftClassLoader;

$GEN_DIR = __DIR__."/genphp";

$loader = new ThriftClassLoader();
$loader->registerNamespace('Thrift', __DIR__ . '/lib/php/lib');
$loader->registerNamespace('T', $GEN_DIR);

$loader->register();

use Thrift\Protocol\TBinaryProtocol;
use Thrift\Transport\TSocket;
use Thrift\Transport\THttpClient;
use Thrift\Transport\TBufferedTransport;
use Thrift\Exception\TException;

$socket = new TSocket('127.0.0.1', 9090);
$transport = new TBufferedTransport($socket, 1024, 1024);
$protocol = new TBinaryProtocol($transport);

$client = new \T\TestTClient($protocol);

$transport->open();

$msg = $client->getdata('12');

print "msg:".$msg."\n";

$transport->close();


