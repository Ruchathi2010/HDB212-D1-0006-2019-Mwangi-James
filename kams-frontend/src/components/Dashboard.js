import React from 'react';
import AdsList from './AdsList.js';
import { Box } from '@chakra-ui/react';

function Dashboard() {
  return (
    <Box p={4} flex="1" overflowY="auto">
      <AdsList />
    </Box>
  );
}

export default Dashboard;
