import React, { useState } from 'react';
import { View, TextInput, Button, Text, Alert, StyleSheet } from 'react-native';
import { registerUser } from './api';

export default function RegisterScreen({ navigation }) {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleRegister = async () => {
    if (!username || !email || !password) {
      Alert.alert('Validation Error', 'All fields are required');
      return;
    }

    try {
      const data = await registerUser(username, email, password);
      Alert.alert('Registration Success', `User ${data.username} created!`);
      // După înregistrare, navighează la login
      navigation.navigate('Login');
    } catch (error) {
      const message = error.response?.data?.detail || error.message;
      Alert.alert('Registration Failed', message);
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
      <Text style={styles.label}>Email:</Text>
      <TextInput
        value={email}
        onChangeText={setEmail}
        style={styles.input}
        keyboardType="email-address"
        autoCapitalize="none"
      />
      <Text style={styles.label}>Password:</Text>
      <TextInput
        value={password}
        onChangeText={setPassword}
        secureTextEntry
        style={styles.input}
      />
      <Button title="Register" onPress={handleRegister} />
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
  title="Login" 
  onPress={() => navigation.navigate('Login')}
/>
