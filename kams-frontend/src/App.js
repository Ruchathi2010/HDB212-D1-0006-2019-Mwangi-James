// src/App.js
import React from 'react';
import Header from './components/Header.js';   // <-- add .js
import Sidebar from './components/Sidebar.js'; // <-- add .js
import Dashboard from './components/Dashboard.js'; // <-- add .js

import { ChakraProvider, Box, Flex } from '@chakra-ui/react';

function App() {
  return (
    <ChakraProvider>
      <Flex h="100vh" bg="gray.100">
        <Sidebar />
        <Box flex="1" display="flex" flexDirection="column">
          <Header />
          <Dashboard />
        </Box>
      </Flex>
    </ChakraProvider>
  );
}

export default App;
