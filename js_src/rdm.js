angular.module('rdmApp', [])
 .config(['$interpolateProvider', function($interpolateProvider) {
  'use strict';
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
 }])

 .controller('UIDController', ['$scope', function(convertor) {
  'use strict';
  convertor.invalid_input_message = 'Invalid UID, please enter a UID in the ' +
   'form MMMM:NNNNNNNN';
  convertor.euid = '';
  convertor.error = '';
  convertor.uid = '';

  convertor.convertToEUID = function() {
   convertor.euid = '';
   convertor.error = '';

   var clean_uid = convertor.uid.replace(/[\.:\-\s]/g, '');
   if (!clean_uid.match(/^[0-9a-fA-F]{12}$/)) {
    convertor.error = convertor.invalid_input_message;
    return;
   }

   var manufacturer_str = clean_uid.slice(0, 4);
   var device_str = clean_uid.slice(4, 12);

   if (manufacturer_str.length !== 4 || device_str.length !== 8) {
    convertor.error = convertor.invalid_input_message;
    return;
   }

   var manufacturer = parseInt(manufacturer_str, 16);
   var device = parseInt(device_str, 16);
   if (isNaN(manufacturer) || isNaN(device)) {
    convertor.error = convertor.invalid_input_message;
    return;
   }

   var euid_bytes = [];

   var manufacturer0 = (manufacturer >> 8) & 0xff;
   var manufacturer1 = manufacturer & 0xff;
   var device0 = (device >> 24) & 0xff;
   var device1 = (device >> 16) & 0xff;
   var device2 = (device >> 8) & 0xff;
   var device3 = device & 0xff;

   euid_bytes.push(manufacturer0 | 0xaa);
   euid_bytes.push(manufacturer0 | 0x55);
   euid_bytes.push(manufacturer1 | 0xaa);
   euid_bytes.push(manufacturer1 | 0x55);

   euid_bytes.push(device0 | 0xaa);
   euid_bytes.push(device0 | 0x55);
   euid_bytes.push(device1 | 0xaa);
   euid_bytes.push(device1 | 0x55);
   euid_bytes.push(device2 | 0xaa);
   euid_bytes.push(device2 | 0x55);
   euid_bytes.push(device3 | 0xaa);
   euid_bytes.push(device3 | 0x55);

   var checksum = euid_bytes.reduce(
    function(previousValue, currentValue, index, array) {
     return previousValue + currentValue;
    }
   );
   var checksum0 = (checksum >> 8) & 0xff;
   var checksum1 = checksum & 0xff;

   euid_bytes.push(checksum0 | 0xaa);
   euid_bytes.push(checksum0 | 0x55);
   euid_bytes.push(checksum1 | 0xaa);
   euid_bytes.push(checksum1 | 0x55);

   convertor.euid = euid_bytes.map(function(i) {
    return i.toString(16);
   }).join(' ');
  };
 }])

 .controller('EUIDController', ['$scope', function(convertor) {
  'use strict';
  convertor.euid = '';
  convertor.error = '';
  convertor.uid = '';

  convertor.convertToUID = function() {
   convertor.error = '';
   convertor.uid = '';

   var clean_euid = convertor.euid.replace(/[,\s]/g, '').trim();
   if (!clean_euid.match(/^[0-9a-fA-F]*$/)) {
    convertor.error = 'Invalid EUID: non hex characters';
    return;
   }

   if (clean_euid.length !== 32) {
    convertor.error =
     'Invalid EUID: insufficent data, should be 32 hex characters';
    return;
   }

   var data = [];
   for (var i = 0; i < 16; i++) {
    var octet = clean_euid.slice(i * 2, (i + 1) * 2);
    var value = parseInt(octet, 16);
    if (isNaN(value)) {
     convertor.error = 'Invalid EUID: bad value' + octet;
     return;
    }
    data.push(value);
   }

   var manufacturer0 = data[0] & data[1];
   var manufacturer1 = data[2] & data[3];
   var manufacturer = (manufacturer0 << 8) + manufacturer1;

   var device0 = data[4] & data[5];
   var device1 = data[6] & data[7];
   var device2 = data[8] & data[9];
   var device3 = data[10] & data[11];

   var device = (device0 << 24) + (device1 << 16) + (device2 << 8) + device3;

   var recovered_checksum = ((data[12] & data[13]) << 8) +
    (data[14] & data[15]);

   var calculated_checksum = data.slice(0, 12).reduce(
    function(previousValue, currentValue, index, array) {
     return previousValue + currentValue;
    }
   );

   if (recovered_checksum !== calculated_checksum) {
    convertor.error = 'Checksum mismatch, was ' + recovered_checksum +
    ', calculated to be ' + calculated_checksum;
    return;
   }

   function zeroPad(num, places) {
    var str = num.toString(16);
    var zero = places - str.length + 1;
    return new Array(+(zero > 0 && zero)).join('0') + str;
   }

   convertor.uid = zeroPad(manufacturer) + ':' + zeroPad(device, 8);
  };
 }]);
