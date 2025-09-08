import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, Button, StyleSheet, Alert } from 'react-native';
import axios from 'axios';

// IP-ul backend-ului tău
const API_URL = 'http://192.168.1.4:8081';

export default function HomeScreen({ navigation }) {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchEvents();
  }, []);

  const fetchEvents = async () => {
    try {
      const response = await axios.get(`${API_URL}/events/`);
      setEvents(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching events:', error.message);
      Alert.alert('Error', 'Could not fetch events from server');
      setLoading(false);
    }
  };

  const handleRegisterEvent = (event) => {
    Alert.alert('Registered', `You have registered for: ${event.name}`);
    // aici mai târziu vei trimite request către backend
  };

  const renderItem = ({ item }) => (
    <View style={styles.item}>
      <Text style={styles.title}>{item.name}</Text>
      <Text>{item.date}</Text>
      <Button title="Register" onPress={() => handleRegisterEvent(item)} />
    </View>
  );

  if (loading) {
    return (
      <View style={styles.container}>
        <Text>Loading events...</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <FlatList
        data={events}
        keyExtractor={(item) => item.id.toString()}
        renderItem={renderItem}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
  },
  item: {
    padding: 15,
    borderWidth: 1,
    borderColor: '#ccc',
    marginBottom: 10,
    borderRadius: 5,
  },
  title: {
    fontWeight: 'bold',
    fontSize: 16,
    marginBottom: 5,
  },
});
