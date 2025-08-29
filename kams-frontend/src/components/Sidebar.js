import React from 'react';
import { Box, VStack, Button } from '@chakra-ui/react';

function Sidebar() {
  return (
    <Box bg="gray.100" width="250px" p={4} boxShadow="md">
      <VStack spacing={4} align="stretch">
        <Button variant="ghost">Dashboard</Button>
        <Button variant="ghost">Ads</Button>
        <Button variant="ghost">Reports</Button>
        <Button variant="ghost">Settings</Button>
      </VStack>
    </Box>
  );
}

export default Sidebar;
