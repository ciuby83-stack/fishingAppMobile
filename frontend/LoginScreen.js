import React, { useState } from 'react';
import { View, TextInput, Button, Text, Alert, StyleSheet } from 'react-native';
import { loginUser } from './api';

export default function LoginScreen({ navigation }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    if (!username || !password) {
      Alert.alert('Validation Error', 'Please enter username and password');
      return;
    }

    try {
      const data = await loginUser(username, password);
      Alert.alert('Login Success', `Welcome ${data.username}`);
      // navigare la alt ecran, ex: HomeScreen
      // navigation.navigate('Home'); 
    } catch (error) {
      // în cazul în care backend-ul FastAPI returnează detail
      const message = error.response?.data?.detail || error.message;
      Alert.alert('Login Failed', message);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.label}>Username:</Text>
      <TextInput
        value={username}
        onChangeText={setUsername}
        style={styles.input}
        autoCapitalize="none"
      />
      <Text style={styles.label}>Password:</Text>
      <TextInput
        value={password}
        onChangeText={setPassword}
        secureTextEntry
        style={styles.input}
      />
      <Button title="Login" onPress={handleLogin} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 20,
    justifyContent: 'center',
    flex: 1,
  },
  label: {
    marginBottom: 5,
    fontWeight: 'bold',
  },
  input: {
    borderWidth: 1,
    borderColor: '#999',
    padding: 10,
    marginBottom: 15,
    borderRadius: 5,
  },
});
<Button
  title="Go to Register"
  onPress={() => navigation.navigate('Register')}
/>

