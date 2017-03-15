<?php
// DO NOT EDIT! Generated by Protobuf-PHP protoc plugin 1.0
// Source: throttlerdata.proto

namespace Vitess\Proto\Throttlerdata {

  class UpdateConfigurationRequest extends \DrSlump\Protobuf\Message {

    /**  @var string */
    public $throttler_name = null;
    
    /**  @var \Vitess\Proto\Throttlerdata\Configuration */
    public $configuration = null;
    
    /**  @var boolean */
    public $copy_zero_values = null;
    

    /** @var \Closure[] */
    protected static $__extensions = array();

    public static function descriptor()
    {
      $descriptor = new \DrSlump\Protobuf\Descriptor(__CLASS__, 'throttlerdata.UpdateConfigurationRequest');

      // OPTIONAL STRING throttler_name = 1
      $f = new \DrSlump\Protobuf\Field();
      $f->number    = 1;
      $f->name      = "throttler_name";
      $f->type      = \DrSlump\Protobuf::TYPE_STRING;
      $f->rule      = \DrSlump\Protobuf::RULE_OPTIONAL;
      $descriptor->addField($f);

      // OPTIONAL MESSAGE configuration = 2
      $f = new \DrSlump\Protobuf\Field();
      $f->number    = 2;
      $f->name      = "configuration";
      $f->type      = \DrSlump\Protobuf::TYPE_MESSAGE;
      $f->rule      = \DrSlump\Protobuf::RULE_OPTIONAL;
      $f->reference = '\Vitess\Proto\Throttlerdata\Configuration';
      $descriptor->addField($f);

      // OPTIONAL BOOL copy_zero_values = 3
      $f = new \DrSlump\Protobuf\Field();
      $f->number    = 3;
      $f->name      = "copy_zero_values";
      $f->type      = \DrSlump\Protobuf::TYPE_BOOL;
      $f->rule      = \DrSlump\Protobuf::RULE_OPTIONAL;
      $descriptor->addField($f);

      foreach (self::$__extensions as $cb) {
        $descriptor->addField($cb(), true);
      }

      return $descriptor;
    }

    /**
     * Check if <throttler_name> has a value
     *
     * @return boolean
     */
    public function hasThrottlerName(){
      return $this->_has(1);
    }
    
    /**
     * Clear <throttler_name> value
     *
     * @return \Vitess\Proto\Throttlerdata\UpdateConfigurationRequest
     */
    public function clearThrottlerName(){
      return $this->_clear(1);
    }
    
    /**
     * Get <throttler_name> value
     *
     * @return string
     */
    public function getThrottlerName(){
      return $this->_get(1);
    }
    
    /**
     * Set <throttler_name> value
     *
     * @param string $value
     * @return \Vitess\Proto\Throttlerdata\UpdateConfigurationRequest
     */
    public function setThrottlerName( $value){
      return $this->_set(1, $value);
    }
    
    /**
     * Check if <configuration> has a value
     *
     * @return boolean
     */
    public function hasConfiguration(){
      return $this->_has(2);
    }
    
    /**
     * Clear <configuration> value
     *
     * @return \Vitess\Proto\Throttlerdata\UpdateConfigurationRequest
     */
    public function clearConfiguration(){
      return $this->_clear(2);
    }
    
    /**
     * Get <configuration> value
     *
     * @return \Vitess\Proto\Throttlerdata\Configuration
     */
    public function getConfiguration(){
      return $this->_get(2);
    }
    
    /**
     * Set <configuration> value
     *
     * @param \Vitess\Proto\Throttlerdata\Configuration $value
     * @return \Vitess\Proto\Throttlerdata\UpdateConfigurationRequest
     */
    public function setConfiguration(\Vitess\Proto\Throttlerdata\Configuration $value){
      return $this->_set(2, $value);
    }
    
    /**
     * Check if <copy_zero_values> has a value
     *
     * @return boolean
     */
    public function hasCopyZeroValues(){
      return $this->_has(3);
    }
    
    /**
     * Clear <copy_zero_values> value
     *
     * @return \Vitess\Proto\Throttlerdata\UpdateConfigurationRequest
     */
    public function clearCopyZeroValues(){
      return $this->_clear(3);
    }
    
    /**
     * Get <copy_zero_values> value
     *
     * @return boolean
     */
    public function getCopyZeroValues(){
      return $this->_get(3);
    }
    
    /**
     * Set <copy_zero_values> value
     *
     * @param boolean $value
     * @return \Vitess\Proto\Throttlerdata\UpdateConfigurationRequest
     */
    public function setCopyZeroValues( $value){
      return $this->_set(3, $value);
    }
  }
}

