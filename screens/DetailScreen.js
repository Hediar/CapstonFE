import React, { useEffect, useState } from 'react';
import {View, Text, StyleSheet, TouchableOpacity, Alert, PermissionsAndroid} from 'react-native';
import RNFetchBlob from 'rn-fetch-blob';

function DetailScreen({route}) {
  const [response] = useState(null);
  const downloadppt = async () => {
    try{
      await RNFetchBlob.config({
        addAndroidDownloads: {
          useDownloadManager: true,
          notification: true,
          appendExt: 'pptx',
          path: `${RNFetchBlob.fs.dirs.DownloadDir}/${file.name}`,
          description: 'Downloading the file',
        },
      })
      .fetch('GET','URL',
      {
        "Content-Type": "multipart/form-data",
        // body: body,
      });
    } catch(error){
      console.log('fail download');
      console.log(error);
    }
  };

  const downloadFile = async() => {
    try{
      const granted = await PermissionsAndroid.request(PermissionsAndroid.PERMISSIONS.WRITE_EXTERNAL_STORAGE);
      if (granted === PermissionsAndroid.RESULTS.GRANTED) {
        downloadppt();
      } else {
        Alert.alert('Permission Denied', 'You need to give storage permission to download the file');
      } 
    }
    catch(error){
      console.log(error);
    }
  }

  return (
    <View style={styles.block}>
      <TouchableOpacity
        onPress={() => {
          downloadFile();
        }}>
        <View style={styles.button}>
          <Text style={styles.buttonText}>PPT 저장하기</Text>
        </View>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  block: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  text: {
    fontSize: 28,
  },
  button: {
    width: 260,
    height: 60,
    alignItems: 'center',
    backgroundColor: '#2196F3',
    padding: 10,
    marginBottom: 30,
    borderRadius: 80
  },
  buttonText: {
    textAlign: 'center',
    padding: 10,
    color: 'white'
  },
});

export default DetailScreen;