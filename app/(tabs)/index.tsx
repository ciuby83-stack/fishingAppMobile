import { Text, View, StyleSheet } from 'react-native';

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>🎣 Salut, frate! Merge aplicația 🚀</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#222',
  },
  text: {
    color: 'white',
    fontSize: 22,
    fontWeight: 'bold',
  },
});
import { Text, View } from "react-native";

export default function App() {
  return (
    <View style={{ flex: 1, justifyContent: "center", alignItems: "center", backgroundColor: "#111" }}>
      <Text style={{ color: "white", fontSize: 24 }}>🚀 Conectat corect la frontend!</Text>
    </View>
  );
}
